# Tax Calculator
# import pandas to read excel sheet and convert to dict
import pandas
xlsx = pandas.read_excel('state_tax_rate.xlsx')
file = xlsx.to_dict("dict")

# param{str}
# return{float}
def get_tax(state_abbrev):
  for i in file["Abbreviation"]:
    if(file["Abbreviation"][i] == state_abbrev):
      tax_rate = file["Tax Rate"][i]
      return tax_rate

# param{float}
# return{str}
def calculate(get_tax):
  object_inp = float(input("Price of Object(Decimal format): "))
  return "Final Price: " + str(object_inp + (get_tax*object_inp))

# param{none}
# return{none}
def get_user_input():
  state_initials = input("Please input State Abbrev in CAPS: ")
  if state_initials:
    print(calculate(get_tax(state_initials)))

get_user_input()
