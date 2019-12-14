#To filter out vowels from string
str = input('Enter the string you want to filter:')
x = ['a','e','i','o','u']
for i in str:
    for n in x:
        if i == n:
            print(i,end=' ')
