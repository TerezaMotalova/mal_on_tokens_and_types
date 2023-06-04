# MAIN FUNCTIONS FOR PROCESSING OF A TEXT BOTH IN PINYIN AND CHINESE CHARACTERS
# NOTE: output data have a tabular form intended to be saved in plain text format (e.g. .txt)


import PY_pinyin_text_processing_script as pinyin_text
import PY_character_text_processing as char_text


# general functions

def load_file(file_name):
    """loads a text from the file as a string"""

    with open(file_name, mode='r', encoding='utf-8') as text:
        text_to_process = text.read()

    return text_to_process


def delete_duplicates(word_list):
    """deletes duplicate occurences of words and returns a list of their types"""

    word_list_without_duplicates = []

    for word in word_list:
        if word not in word_list_without_duplicates:
            word_list_without_duplicates.append(word)

    return word_list_without_duplicates


def save_file(word_list, file_name, headers):
    """saves data in their tabular form using white characters (as delimiters)"""

    with open(file_name, mode="w", encoding="utf-8") as a_file:
        for header in headers:
            print(header, end='\t', file=a_file)
        print(file=a_file)
    
        for word in word_list:
            for item in word:
                print(item, end="\t", file=a_file)
            print(file=a_file)


# MAIN FUNCTIONS:
def process_pinyin_texts(piniyn_input, txt_token_output, txt_type_output):
    """calls respective functions to process and quantify a text in pinyin 
       and saves results for both tokens and types
       input arguments: 
            pinyin_input: a list with input filename(s),
            txt_token_output: a list with output filename(s) for tokens
            txt_type_output: a list with output filename(s) for types"""

    headers = ['pinyin', 'phoneme', 'syll', 'syll_n', 'letter_n', 'sound_n']

    for text in range(len(piniyn_input)):

        # PREPARING DATA
        loaded_text = load_file(piniyn_input[text])
        text_without_punctuation = pinyin_text.delete_punctuation(loaded_text)
        word_list = pinyin_text.prepare_word_list(text_without_punctuation)

        # PROCESSING DATA
        word_list = pinyin_text.process_pinyin_words(word_list)

        # TOKENS
        save_file(word_list, txt_token_output[text], headers)

        # TYPES
        word_list_types = delete_duplicates(word_list)
        save_file(word_list_types, txt_type_output[text], headers)


def process_char_texts(char_input, txt_token_output, txt_type_output):
    """calls respective functions to process and quantify a text in Chinese characters
       and saves results for both tokens and types
       input arguments: 
            char_input: a list with input filename(s),
            txt_token_output: a list with output filename(s) for tokens
            txt_type_output: a list with output filename(s) for types"""

    headers = ['char', 'char_n', 'com_n', 'stroke_n']

    for text in range(len(char_input)):
        
        # PREPARING DATA
        loaded_text = load_file(char_input[text])
        word_list = char_text.word_segmentation(loaded_text)
        word_list = char_text.delete_punctuation(word_list)

        # PROCESSING DATA
        word_list = char_text.count_graphic_lengths(word_list)

        # TOKENS
        save_file(word_list, txt_token_output[text], headers)

        # TYPES
        word_list_types = delete_duplicates(word_list)
        save_file(word_list_types, txt_type_output[text], headers)


# EXAMPLE OF RUNNING THE SCRIPT:
process_pinyin_texts(['new_testament_40_66_pinyin_text.txt'], 
                     ['new_testament_40_66_pinyin_token.txt'],
                     ['new_testament_40_66_pinyin_type.txt'])

process_char_texts(['new_testament_40_66_character_text.txt'], 
                     ['new_testament_40_66_character_token.txt'],
                     ['new_testament_40_66_character_type.txt'])
