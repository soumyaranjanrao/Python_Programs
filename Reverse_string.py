#To reverse a entered string
def reverse(string):
    reversed = ''
    for i in string:
        reversed = i+reversed
    print('The reverse string is:', reversed)

string = input('Enter the string you want to reverse:')
print('You entered:', string)
reverse(string)
