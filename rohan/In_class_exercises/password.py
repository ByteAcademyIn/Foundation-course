'''
Question:
A website requires the users to input username and password to register. Write
a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
'''
import re
pwd = input("Enter password: ")

if not (re.search('[a-z]+', pwd) and re.search('[0-9]+', pwd) and re.search('[A-Z]+', pwd) and re.search('[$#@]+', pwd)):
    print('Error invalid password')