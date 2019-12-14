#To print the range of perfect numbers
num1 = int(input('Enter the number from where to start:'))
num2 = int(input('Enter the number to where you want to end:'))
for num in range(num1,num2+1):
    result = 0
    for i in range(1,num):
        if (num%i==0):
            result = result+i
    if num == result:
        print(num)
