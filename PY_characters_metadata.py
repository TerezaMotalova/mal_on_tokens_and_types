# FUNCTIONS FOR PROCESSING METADATA ABOUT CHINESE CHARACTERS (using the source below)
# SOURCE: Beijing Language and Culture University, BCC语料库 - 北京语言大学 (hzinfo.txt), available at:
# http://bcc.blcu.edu.cn/downloads/resources/%E6%B1%89%E5%AD%97%E4%BF%A1%E6%81%AF%E8%AF%8D%E5%85%B8.zip


from codecs import open


def load_file(file_name):
    """loads the file with data about Chinese characters"""

    with open(file_name, mode='r', encoding='gb18030') as text:
        list_to_process = [line for line in text]

    return list_to_process


def process_stroke_n(a_string):
    """processes a string containing a number of strokes and returns the number as an integer"""

    a_string = a_string.split(':')

    return int(a_string[1].strip())


def process_pinyin(a_string):
    """processes a string containing pinyin and returns it"""

    a_string = a_string.split(':')

    return a_string[1].strip()


def process_component(a_string):
    """processes a string containing components and returns its list"""

    a_string = a_string.split(':')
    components = a_string[1].split()
    component_list = [item.strip() for item in components]

    return component_list


def create_dict(list_to_process):
    """creates a dictionary for each character containing
       numbers of its stroke(s) and component(s), a list of the component(s), pinyin transcription,
       (saves data if needed) and returns a dictionary of all processed characters"""

    char_dict = {}
    item_n = 0

    while item_n < len(list_to_process):
        if list_to_process[item_n].startswith('#'):
            char_dict[list_to_process[item_n][1]] = {}
            char_dict[list_to_process[item_n][1]]['stroke_n'] = process_stroke_n(list_to_process[item_n + 1])
            char_dict[list_to_process[item_n][1]]['pinyin'] = process_pinyin(list_to_process[item_n + 2])
            char_dict[list_to_process[item_n][1]]['component'] = process_component(list_to_process[item_n + 3])
            char_dict[list_to_process[item_n][1]]['component_n'] = len(char_dict[list_to_process[item_n][1]]['component'])
            item_n += 4

    # with open('characters_metadata_dictionary.txt', mode='w', encoding='gb18030') as boo:
    #     print(char_dict, file=boo)

    return char_dict


def char_dict_main():
    """main function for processing the above mentioned file as a dictionary"""

    list_to_process = load_file('hzinfo.txt')

    return create_dict(list_to_process)