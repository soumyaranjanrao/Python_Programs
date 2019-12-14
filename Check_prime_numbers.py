#To check whether the number is a prime or not
num = int(input('Enter the number you want to check:'))
if num>1:
    for i in range(2,num):
        if (num%i==0):
            break
    else:
        print('The number is prime:', num)
