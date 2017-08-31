import re

email = input('Enter email address: ')

#name = email[0:email.index('@')]   this can also be done by this.
#print('Name:', name)

print('Name:', (re.search(r'\w*', email)).group().title())
