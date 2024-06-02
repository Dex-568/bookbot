def main():
    path = "books/frankenstein.txt"
    text = grab_file(path)
    wc = word_count(text)
    char_dict = char_count(text)
    sorted = to_list(char_dict)
    print(sorted)

    print(f"--- Begin report of {path} ---")
    print(f"{wc} words found")
    print()

    for item in sorted:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End Report")

def grab_file(path):
    with open(path) as f:
        return f.read()
    
def word_count(text):
    words = text.split()
    return len(words)

def sort_on(dict):
    return dict["num"]

def char_count(text):
    counted = {}
    low_text = text.lower()

    for char in low_text:
        if char in counted:
            counted[char] += 1
        else:
            counted[char] = 1
    return counted

def to_list(char_dict):
    sorted = []
    for char in char_dict:
        sorted.append({"char": char, "num": char_dict[char]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted

main()