a, b, c = map(float, input().split(', '))
P = a+b+c
prmtr = P * 0.5
S = (prmtr * (prmtr-a) * (prmtr-b) * (prmtr-c))**0.5
print('P=', P, 'S=', S)