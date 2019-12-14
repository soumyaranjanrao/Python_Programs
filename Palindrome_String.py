#To print the given  string is palindrome or not
string = input('Enter your string:')
print('You entered:', string)
rev_string = string[::-1]
print('The reverse of the string is:', rev_string)
if string==rev_string:
    print('You have entered a palindrome input')
else:
    print('You have entered a normal input')
