num = int(input('Enter your number you want to reverse:'))
result = 0
while num!=0:
    digit = num%10
    result = result*10+digit
    num = num//10
print('The reverse number is:', result)
