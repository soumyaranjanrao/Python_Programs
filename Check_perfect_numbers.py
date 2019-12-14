#To check whether the number is perfect or not
num = int(input('Enter the number to check whether the number is perfect or not:'))
result = 0
for i in range(1,num):
    if (num%i==0):
        result = result+i
if num == result:
    print('The number is perfect:', num)
else:
    print('The number is not perfect:', num)
    
