# random and string modules
import random
import string

# global vars --> using the 'string' module to generate letters, numbers, and characters
letters = string.ascii_letters
numbers = string.digits
characters = string.punctuation
shuffledLetters = ''.join(random.sample(letters, len(letters)))
shuffledNumbers = ''.join(random.sample(numbers, len(numbers)))
shuffledCharacters = ''.join(random.sample(characters, len(characters)))
on = True

print('')
while on:
    shuffledLetters = ''.join(random.sample(letters, len(letters)))
    shuffledNumbers = ''.join(random.sample(numbers, len(numbers)))
    shuffledCharacters = ''.join(random.sample(characters, len(characters)))
    print('')
    ask = input('[g] to generate pass => ')
    print('')

    if ask == 'g':
        for item in range(random.randint(5, 8)):  # ! For each number between 5 and 8 inclusive, each list will find
            # the corresponding element.
            print(shuffledLetters[item] + shuffledNumbers[item] + shuffledCharacters[item], end='')
        print('')

    elif ask == 'q':
        on = False
        quit()
    else:
        print('Invalid Input')
print('')
