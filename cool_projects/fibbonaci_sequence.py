# determine whether a list of numbers follows the fibonacci sequence
# fibbonaci sequence --> [0,1,1,2,3,5,8,13] --> add up the previous two numbers to get the next number in list

def determine_fib(list):
    count = 0
    for num in range(2, len(list)):
        if int(list[num]) == int(list[num - 2]) + int(list[num - 1]):
            count += 1
    if count == len(list) - 2:
        return str(list) + ' is a fibinacci sequence'
    return str(list) + ' is not a fibinacci sequence'

print(determine_fib([0,2,4,6,7]))
