#To check the given number is armstrong or not
num = int(input('Enter the number you want to check armstrong or not:'))
i = num
result = 0
n = len(str(i))
while (i!=0):
    digit = i%10
    result = result+digit**n
    i = i//10
print(result)
if num==result:
    print('Number is armstrong number:', num)
