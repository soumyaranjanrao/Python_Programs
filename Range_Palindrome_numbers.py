#To check whether a number is a palindrome or not
num = int(input('enter your number:'))
for i in range(num+1):
    i = str(i)
    rev_i = i[::-1]
    if i == rev_i:
        print(i)
