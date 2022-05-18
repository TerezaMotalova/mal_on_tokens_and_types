# FUNCTIONS FOR PROCESSING OF A TEXT IN CHINESE CHARACTERS
# FUNCTIONS FOR QUANTIFICATION OF WORD LENGTHS (in numbers of Chinese characters, components, strokes)


import PY_characters_metadata as CH_metadata
import pynlpir


# functions for text processing

def word_segmentation(a_text):
    """segments a text into words and returns a list of words"""

    pynlpir.open()
    word_list = pynlpir.segment(a_text, pos_tagging=False)
    pynlpir.close()

    return word_list


def delete_punctuation(word_list):
    """loops through a list of words, deletes punctuation marks and returns modified list"""

    punctuation = '，！？；：（）。「」、‧《》〈〉,() '

    word_list_without_punctuation = []

    for word in word_list:
        if len(word) != 0 and word.strip() not in punctuation:
            word_list_without_punctuation.append([word.strip()])

    return word_list_without_punctuation


# functions for quantification of word lengths (in characters, components, strokes)

def count_component_stroke(word, char_dict):
    """counts a word's length in number of components and strokes and returns the numbers as integers"""

    component_n = 0
    stroke_n = 0

    for character in word:
        if character in char_dict:
            component_n += char_dict[character]['component_n']
            stroke_n += char_dict[character]['stroke_n']
        else:  # if character's data is not available
          return 0, 0

    return component_n, stroke_n


def count_graphic_lengths(word_list):
    """adds numbers of characters, components and strokes for each word in a word list"""

    char_dict = CH_metadata.char_dict_main()

    for word in word_list:
        component_n, stroke_n = count_component_stroke(word[0], char_dict)
        # checks if data for given characters of a word is available
        if component_n != 0:
            word.append(len(word[0]))
        else:
            word.append(0)
        word.append(component_n)
        word.append(stroke_n)

    return word_list
