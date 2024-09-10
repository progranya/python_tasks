m = int(input())
e = m % 10
d = m%100//10
c = m%1000//100
b = m%10000//1000
a = m//10000
f = (d**e)*c/(a-b)
print(f)
print(a, b, c, d, e)
