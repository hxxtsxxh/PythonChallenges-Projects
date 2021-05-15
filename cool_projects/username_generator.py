import random as r

on = True


def create_custom_username(name):
    addons = ['fire'.casefold(),
              'cold'.casefold(),
              'ninja'.casefold(),
              'cool'.casefold(),
              'xD'.casefold(),
              'princess'.casefold(),
              'ginger'.casefold(),
              'cracker'.casefold(),
              'genius'.casefold(),
              'angel'.casefold(),
              'sir'.casefold(),
              'poop'.casefold(),
              'monkey'.casefold(),
              'chunky'.casefold()]

    while on:
        print('')
        inp = input('[g] to generate username >> ')
        print('')
        if inp == 'g'.casefold():
            print(str(r.randint(0, 20)) + addons[r.randint(0, len(addons) - 1)] + name)
        elif inp == 'q'.casefold():
            quit()
        else:
            print('Type a valid input!')


user = input('Enter name: ')
print('')
create_custom_username(user)
