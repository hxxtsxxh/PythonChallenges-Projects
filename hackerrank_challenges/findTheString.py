# find the number of occurences of a substring in a string

def countOcc(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            count += 1
    return count


print(countOcc("banana", "ana"))
