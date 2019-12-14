import random
lst = [0,1,2,3,4,5,6,7,8]
def show():
    print(lst[0],'|',lst[1],'|',lst[2])
    print('---------')
    print(lst[3],'|',lst[4],'|',lst[5])
    print('---------')
    print(lst[6],'|',lst[7],'|',lst[8])

while True:
    num = int(input('Select a Spot:'))
    if lst[num]!='x' and lst[num]!='o':
        lst[num]='x'

        find = True
        while find:
            random.seed()
            oppo = random.randint(0,8)
            
            if lst[oppo]!='o' and lst[oppo]!='x':
                lst[oppo]='o'
                find=False
    else:
        print('The spot is taken')

    show()
