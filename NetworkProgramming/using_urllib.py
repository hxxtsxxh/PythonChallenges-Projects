import urllib.request, urllib.parse, urllib.error

f_hand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in f_hand:
    print(line.decode().strip())