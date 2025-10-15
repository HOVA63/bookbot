def get_num_words(file_content):
    return len(file_content.split())

def get_num_character(file_content):
    file_content = file_content.lower()
    characters = {}
    for i in file_content:
        characters[i] = characters.get(i, 0) + 1
    return characters