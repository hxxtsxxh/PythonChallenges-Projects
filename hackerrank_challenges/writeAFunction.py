leap_years = [2000, 2400]
not_leap_years = [1800, 1900, 2100, 2200, 2300, 2500]

def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        if year in leap_years:
            leap = True
        elif year in not_leap_years:
            leap = False
        leap = True
    if year % 100 == 0:
        if year in leap_years:
            leap = True
        elif year in not_leap_years:
            leap = False
        leap = False
    if year % 400 == 0:
        if year in leap_years:
            leap = True
        elif year in not_leap_years:
            leap = False
        leap = True
    
    return leap

year = int(input())
print(is_leap(year))

