def get_num_words(text):
    num_words = len(text.split())
    return num_words  

def get_chars_count(text):
    small_cap = text.lower()
    result = {}
    for c in small_cap:
        if c in result:
            result[c] += 1
        else:
            result[c] = 1
    return result  

def sort_char_by_count(char_dict):
        result_list = []
        for char, count in char_dict.items():
             char_info = {'char': char, 'count': count}
             result_list.append(char_info)
        
        result_list.sort(key=lambda x: x['count'], reverse=True)
        return result_list

