# create a function that returns the total sum of internal angles of a polygon

def sum_polygon(sides):
    formula = (sides-2) * 180
    return formula

print(sum_polygon(6))