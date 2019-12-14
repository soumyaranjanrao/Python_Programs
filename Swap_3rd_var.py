#To swap 2 numbers by using 3rd variable
num1 = int(input('Enter your 1st number:'))
num2 = int(input('Enter your 2nd number:'))
temp = num1
num1 = num2
num2 = temp
print('After swapping your 1st numbers:{} and the second number is:{}'.format(num1,num2))
