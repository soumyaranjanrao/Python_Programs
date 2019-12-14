from itertools import permutation
num = int(input('Enter the number of the combination you want:'))
for i in range(num+1):
    print(f'The permutation is: {permutation.permutation(i)}')
