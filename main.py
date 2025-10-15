from stats import get_num_words

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content

def main():
    book_text = get_book_text("/home/hova/workspace/github.com/HOVA63/bookbot/books/frankenstein.txt")
    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")

main()