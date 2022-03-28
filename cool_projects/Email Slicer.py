"""
Email Slicer:

This is one of the convenient python projects that has a lot of use in the future. The program
helps get you the username and domain name from an email address. You can even customize the application and send a
message to the host with this information.

"""
emails = []
on = True


def process_email(email_address):
    if "@" in email_address:
        new_email = email_address.split('@')
        username = new_email[0]
        domain = new_email[1]
        emails.append('Username: ' + username + '   Domain: ' + domain)
    elif enter_email == 's':
        print('')
        print(*emails, sep="\n")
        print('')
    elif enter_email == 'q':
        print('')
        print('Goodbye!')
        quit()
    else:
        print('Invalid Input')
        print('')


while on:
    enter_email = input('Enter Email: ')
    process_email(enter_email)
