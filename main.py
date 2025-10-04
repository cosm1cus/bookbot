from stats import word_count, symbol_count, sort_symbol_count, sort_symbol_count

def main():
    book_path = "books/frankenstein.txt"
    text = get_boot_text(book_path)
    count = word_count(text)
    symbol = symbol_count(text)
    sorted_symbol = sort_symbol_count(symbol)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for i in sorted_symbol:
        print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

def get_boot_text(path):
    with open(path) as f:
        return f.read()

main()