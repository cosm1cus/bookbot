def main():
    book_path = "books/frankenstein.txt"
    text = get_boot_text(book_path)
    print(text)

def get_boot_text(path):
    with open(path) as f:
        return f.read()

main()