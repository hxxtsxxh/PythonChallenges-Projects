# create a function that takes two numbers and a mathematical operator and will perform a calculation 

def calculator(x, operator, y):
    if operator == "+":
        return x + y
    elif operator == "-":
        return x - y
    elif operator == "*":
        return x * y
    elif operator == "/":
        if y == 0:
            return "Can't divide by 0!"
        return x / y
    else:
        return "Invalid."
    

print(calculator(4,"/",0))