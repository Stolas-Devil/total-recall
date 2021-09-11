

a = []

def func(x):
    final = []
    for i in x:
        is_min = False
        for j in str(i):
            if j == '-':
                is_min = True
            else:
                final.append(int(j))
    return sum(final)

for i in range(int(input().split()[0])):
    a.append([int(i) for i in input().split()])



a = a[::-1]

for i in range(len(a)):
    for j in a[i]:
        print(j, end=' ')
    if i != len(a) - 1:
        print('')


