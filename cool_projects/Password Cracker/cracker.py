import hashlib  # Importing hashlib will help create SHA-1 hashes.
from urllib.request import urlopen  # this method will help to open and read wordlist file via and URL!

'''Now, we are going to create individual functions for tasks like hashing, 
reading wordlist file and then finally for Brute Forcing!'''


# this function will take a URL as a parameter and will then return us file content
# if any exception is raised during this process, the program will exit() the script
def read_wordlist(url):
    global wordlistfile
    try:
        wordlistfile = urlopen(url).read()
    except Exception as e:
        print("Hey there was some error while reading the wordlist, error:", e)
        exit()
    return wordlistfile


# this function will take passwd as a parameter and then will return us hash of the password as a string the
# hashlib.sha1 function expects the argument to be of type<class 'bytes'> which is why we are passing passwd.encode()
def hash(passwd):
    result = hashlib.sha1(passwd.encode())
    return result.hexdigest()


# this function will take just compare the hash of both the wordlist item and the password
# if both are equal, then it will return the equivalent passwords in the wordlist.
def bruteforce(guesspasswordlist, actual_password_hash):
    for guess_password in guesspasswordlist:
        if hash(guess_password) == actual_password_hash:
            print("Hey! your password is:", guess_password, "\n please change this, it was really easy to guess it (:")
            # if the password is found then it will terminate the script here
            exit()


# the url below can be ANY URL; just make sure it is a txt file!
url = 'https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/master/Real-Passwords/Top12Thousand-probable-v2' \
      '.txt '
actual_password = 'computers'
actual_password_hash = hash(actual_password)

wordlist = read_wordlist(url).decode('utf-8')
guesspasswordlist = wordlist.split('\n')

# running the Brute Force attack
bruteforce(guesspasswordlist, actual_password_hash)

# The line below would be executed if your password was not there in the wordlist
print("Hey! I couldn't guess this password, it was not in my wordlist, this is good news! you win (: ")

