# create a function that takes in a triangle's base and height to find the area.

def tri_area(x, y):
    product = x * y
    return product/2

b = float(input('Base: '))
h = float(input('Height: '))
print(tri_area(b, h))
