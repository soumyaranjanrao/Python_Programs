#To calculate the GCD by recursive function
def compute(a,b):
    if b == 0:
        return a
    else:
        return(b,a%b)
num1,num2 = [int(i) for i in input('Enter 2 numbers to calculate the gcd:').split(',')]
obj = compute(num1,num2)
print('The result of the gcd is:', obj)
