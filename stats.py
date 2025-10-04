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

def sort_on(item):
    return item["num"]

def sort_symbol_count(raw_text):
    sorted_symbol_tuple = []
    for i in raw_text:
        char = i
        num = raw_text[i]
        if char.isalpha() == True:
            combined_dict = {"char":char, "num":num}
            sorted_symbol_tuple.append(combined_dict)
    sorted_symbol_tuple.sort(reverse=True, key=sort_on)
    return sorted_symbol_tuple