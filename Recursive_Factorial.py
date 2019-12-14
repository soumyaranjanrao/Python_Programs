#To calculate the factorial by recursive method
def compute(num):
    if num == 0:
        result=1
    else:
        result = num*compute(num-1)
    return result
num = int(input('Enter the number you want to calculate the factorial:'))
compute(num)
print('Factorial is:', compute(num))
