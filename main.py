from stats import word_count, symbol_count

def main():
    book_path = "books/frankenstein.txt"
    text = get_boot_text(book_path)
    count = word_count(text)
    symbol = symbol_count(text)
    print(text)
    print(f"Found {count} total words")
    print(symbol)

def get_boot_text(path):
    with open(path) as f:
        return f.read()

main()