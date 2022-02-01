# checks if word is the same backwards
# returns boolean value (True if palindrome, False if not palindrome)

def check(word):
    empty = ''
    for char in word:
        empty = char + empty
    if empty == word:
        return True
    return False


word_input = input("Input a word: ")
print(check(word_input))
