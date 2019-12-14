#To check whether a number is a palindrome or not
num = int(input('enter your number:'))
num = str(num)
print('U entered:', num)
rev_num = num[::-1]
print('After reverse:', rev_num)
if num == rev_num:
    print('Palindrome number')
else:
    print('Not a palindrome number')
