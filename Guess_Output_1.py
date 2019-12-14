#To check the digits of a given list is equal to 21
arr = [2,4,6,3,7,11,15]
for x in arr:
    for y in arr:
        if (x*y==21):
            print(x,y)
