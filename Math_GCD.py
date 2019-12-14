#To calculate the GCD of a number
import math
num1,num2 = [int(i) for i in input('Enter the 2 number you want to calculate the gcd:').split(',')]
result = math.gcd(num1,num2)
print('The result of the gcd is:', result)
