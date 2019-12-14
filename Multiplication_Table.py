#To find the multiplication table
num = int(input('Enter the multliplication table you want:'))
for x in range(1,21):
    print('{}x{}={}'.format(num,x,num*x))
