def pf(sal):
    res = sal*12.5/100
    return res

def itax(sal):
    annual = sal*12
    res = annual*10/100
    return res

sal = float(input('Enter your salary:'))
r1 = pf(sal)
r2 = itax(sal)
print(f'The Provident fund is: {r1} and the Income Tax is: {r2}')
