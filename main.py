from stats import get_num_words, get_chars_dict, sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    book_path = "/home/hova/workspace/github.com/HOVA63/bookbot/books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    chars_dict = get_chars_dict(book_text)
    sorted_dict = sort_dict(chars_dict)
    print_report(num_words, sorted_dict, book_path)
    
def print_report(num_words, sorted_dict, book_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    for item in sorted_dict:
        if not item["char"].isalpha():
            continue
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()