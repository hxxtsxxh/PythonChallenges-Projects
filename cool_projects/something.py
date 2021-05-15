"""
Email Slicer:

This is one of the convenient python projects that has a lot of use in the future. The program
helps get you the username and domain name from an email address. You can even customize the application and send a 
message to the host with this information.

"""
emails = []
on = True


def proccess_email(email_address):
    if "@" in email_address:
        new_email = email_address.split('@')
        emails.append((new_email[0], new_email[1]))
    elif enter_email == 's':
        print(emails)
    else:
        print('Invalid Input')


while on:
    enter_email = input('Enter Email: ')
    proccess_email(enter_email)
