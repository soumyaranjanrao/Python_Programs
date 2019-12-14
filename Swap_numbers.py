#Swapping of numbers not using 3rd variable
num1 = int(input('Enter your 1st number:'))
num2 = int(input('Enter your 2nd number:'))
num1 = num1+num2
num2 = num1-num2
num1 = num1-num2
print('After swapping your 1st number is:%d and the 2nd number is:%d' %(num1,num2))
