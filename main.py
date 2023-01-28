book_path = r'/home/usr/workspace/github.com/tondejphajin/bookbot/books/frankenstein.txt'

def count_words(str):
    words = str.split()
    return len(words)

def count_letters(str):
    result = dict()
    str = str.lower()
    for letter in str:
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1
    return result

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def sort_method(dict):
    return dict["num"]

def dict_to_list(dict):
    new_list = []
    for key in dict:
        new_list.append({"char": key, "num": dict[key]})
    new_list.sort(reverse = True,key=sort_method)
    return new_list

def main():
    book_text = get_book_text(book_path)
    total_words = count_words(book_text)
    total_letters = count_letters(book_text)
    sorted_list = dict_to_list(total_letters)

    print(f'--- File location: {book_path} ---')
    print(f'Total words found in this document: {total_words}')

    for element in sorted_list:
        if not element["char"].isalpha():
            continue
        print(f'The character \'{element["char"]}\' was found {element["num"]} times.')
    
    print("--- End report ---")

    

if __name__ == "__main__":
    main()