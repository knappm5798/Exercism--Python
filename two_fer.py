def two_fer(name):
     print("One for",name,",""One for me.")

name = input('Whats your name? ')
if name=="":
    print('One for you, One for me.')
else:
    two_fer(name)