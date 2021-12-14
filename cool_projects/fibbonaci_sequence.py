# determine whether a list of numbers follows the fibonacci sequence
# Fibonacci sequence --> [0,1,1,2,3,5,8,13] --> add up the previous two numbers to get the next number in list

def determine_fib(l):
    count = 0
    for num in range(2, len(l)):
        if int(l[num]) == int(l[num - 2]) + int(l[num - 1]):
            count += 1
    if count == len(l) - 2:
        return str(l) + ' is a Fibonacci sequence'
    return str(l) + ' is not a Fibonacci sequence'


print(determine_fib([0, 1, 1, 2, 3]))
