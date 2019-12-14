def perm(lst):
    if len(lst) == 0:
        yield []
    elif len(lst) == 1:
        yield [lst]
    else:
        l = 0
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[:i] + lst[i+1:]
            for p in perm(xs):
                yield ([x]+p)

data = list('abcde')
print('Permutation is:')
for p in perm(data):
    print(p)
