def main():
    book_path = "books/frankenstein.txt"
    text = get_boot_text(book_path)
    count = word_count(text)
    print(text)
    print(f"Found {count} total words")

def get_boot_text(path):
    with open(path) as f:
        return f.read()

def word_count(book):
    word_list = book.split()
    return len(word_list)

main()