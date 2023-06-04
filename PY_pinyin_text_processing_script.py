# FUNCTIONS FOR PROCESSING OF A TEXT IN PINYIN
# FUNCTIONS FOR QUANTIFICATION OF WORD LENGTHS (in numbers of syllables, phonemes, pinyin letters)


import re


# functions for text processing

def delete_punctuation(a_text):
    """deletes respective punctuation marks in a text a returns its modified version"""

    new_text = ''

    for letter in a_text:
        if letter.isalnum() or letter.isspace():
            new_text = new_text + letter
        else:
            new_text = new_text + ' '

    return new_text


def prepare_word_list(a_text):
    """segments a text into words based on spaces, prepares all words for their further processing,
       i.e. segmentation into syllables and conversion into phonemes while using alternative symbols"""

    splitted_text = a_text.split()
    word_list = []

    for word in splitted_text:
        word = word.strip().lower()
        word_list.append([word, word, word])

    return word_list


# functions for conversion of pinyin letters into phonemes while using alternative symbols
# covenversion is applied only if there is not one-to-one correspondence between a pinyin letter and a phoneme

def replace_initials(a_word):
    """checks a word for three initials and replaces them by an alternative character '$'"""

    initials = ['ch', 'sh', 'zh']

    for initial in initials:
        if initial in a_word:
            a_word = a_word.replace(initial, '$')

    return a_word


def replace_diphthongs(a_word):
    """checks a word for diphthongs and replaces them by a character '#'"""

    diphthongs = ['ai', 'ao', 'ei', 'ou']

    for diphthong in diphthongs:
        if diphthong in a_word:
            a_word = a_word.replace(diphthong, '#')

    return a_word


def replace_yue_yuan(a_word):
    """checks a word for syllables 'yue' and 'yuan' and replaces them by their modified versions"""

    if 'yue' in a_word:
        a_word = a_word.replace('yue', 'ɥe')
    if 'yuan' in a_word:
        a_word = a_word.replace('yuan', 'ɥæn')

    return a_word


def replace_o(a_word):
    """checks a word for syllables 'bo', 'fo', 'mo', 'po' and replaces the letter 'o' by 'wo'
       NOTE: syllables 'fou', 'mou' and 'pou' will not be affected due to the execution of the previous function (replace_diphthongs)"""

    bofomopos = ['bo', 'fo', 'mo', 'po']

    for bofomopo in bofomopos:
        if bofomopo in a_word:
            a_word = a_word.replace(bofomopo, bofomopo[0] + 'wo')

    return a_word


def replace_ing(a_word):
    """checks a word for 'ing¨' and replaces 'i' by 'jə' (inserting a schwa) with the exception of 'ying'"""

    st_index = 0

    for _ in range(a_word.count('ing')):
        if a_word[(a_word.find('ing', st_index) - 1)] != 'y':
            a_word = a_word[:(a_word.find('ing', st_index))] + 'jə' + a_word[(a_word.find('ing', st_index) + 1):]
        st_index += 3

    return a_word


def replace_un(a_word):
    """checks a word for 'un' and replaces it by 'wən' with the exception of 'jun', 'qun', 'xun' and 'yun'"""

    initials = 'jqxy'  # jun, qun, xun, yun
    st_index = 0

    for _ in range(a_word.count('un')):
        if a_word[(a_word.find('un', st_index) - 1)] not in initials:
            a_word = a_word[:(a_word.find('un', st_index))] + 'wə' + a_word[(a_word.find('un', st_index) + 1):]
        st_index += 2

    return a_word


def replace_nasal_ng(a_word):
    """checks a word for 'ng' and replaces it by 'ŋ'"""

    if 'ng' in a_word:
        a_word = a_word.replace('ng', 'ŋ')

    return a_word


# functions for quantification of word lengths (in syllables, phonemes, pinyin letters)

def process_syllables(a_word):
    """splits a word based on numeric tone marks and returns a list of syllables and its number"""

    a_word = re.split(r'[0-4]', a_word)

    for syllable in a_word:
        if len(syllable) == 0:
            a_word.remove(syllable)

    return a_word, len(a_word)


def count_graphemes(a_word):
    """counts number of graphemes in a word"""

    grapheme_n = 0

    for grapheme in a_word:
        if grapheme != "'" and grapheme != '’' and not grapheme.isdigit():
            grapheme_n += 1

    return grapheme_n


def process_pinyin_words(word_list):
    """calls all functions related to processing of a word in pinyin 
       and returns a list of all processed words with their quantified lenghts"""

    for word in word_list:
        word[1] = replace_initials(word[1])
        word[1] = replace_diphthongs(word[1])
        word[1] = replace_yue_yuan(word[1])
        # word[1] = replace_o(word[1])
        word[1] = replace_ing(word[1])
        word[1] = replace_un(word[1])
        word[1] = replace_nasal_ng(word[1])
        word[2], syllable_n = process_syllables(word[2])
        word.append(syllable_n)
        letter_n = count_graphemes(word[0])
        word.append(letter_n)
        sound_n = count_graphemes(word[1])
        word.append(sound_n)

    return word_list
