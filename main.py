from stats import word_count, symbol_count, sort_symbol_count, sort_symbol_count
import sys

def main():
    book_path = sys.argv
    if len(book_path) <= 1:
        raise Exception("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_boot_text(book_path)
    count = word_count(text)
    symbol = symbol_count(text)
    sorted_symbol = sort_symbol_count(symbol)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for i in sorted_symbol:
        print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

def get_boot_text(path):
    with open(path[1]) as f:
        return f.read()

main()