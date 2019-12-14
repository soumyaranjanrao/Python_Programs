#To find the prime numbers
num1 = int(input('Enter your first number:'))
num2 = int(input('Enter your second number:'))
for num in range(num1,num2+1):
    if num>1:
        for i in range(2,num):
            if (num%i==0):
                break
        else:
            print(num)
