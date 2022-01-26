import random as r

on = True


def create_custom_username(name):
    words_file = open("adj.txt", "r")
    words = words_file.read().splitlines()
    words_file.close()

    while on:
        print('')
        inp = input('[g] to generate username >> ')
        print('')
        if inp == 'g'.casefold():
            print(str(r.randint(0, 20)) + words[r.randint(0, len(words) - 1)] + name)
        elif inp == 'q'.casefold():
            quit()
        else:
            print('Type a valid input!')


user = input('Enter name: ')
print('')
create_custom_username(user)