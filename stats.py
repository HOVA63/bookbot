def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for i in text:
        lowered = i.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_dict(char_dict):
    sorted_dict_list = []
    for key, value in char_dict.items():
        sorted_dict_list.append({"char": key, "num": value})
    def sort_on(items):
        return items["num"]
    sorted_dict_list.sort(reverse=True, key=sort_on)
    return sorted_dict_list