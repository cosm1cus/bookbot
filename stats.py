def word_count(book):
    word_list = book.split()
    return len(word_list)

def symbol_count(text):
    book_text = text.lower()
    dict_symbol = {}
    for i in book_text:
        if i not in dict_symbol:
            dict_symbol[i] = 1  
        else:
            dict_symbol[i] = dict_symbol[i] + 1
    return dict_symbol