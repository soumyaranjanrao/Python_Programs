num1 = int(input('Enter the first number:'))
num2 = int(input('Enter your second number:'))
if num1>num2:
    min = num1
else:
    min = num2
while True:
    if (min%num1 == 0) and (min%num2 == 0):
        print(f'LCM is: {min}')
        break
    min = min+1
