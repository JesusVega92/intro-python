a = [1,2,3,4,5]
b = a 
c = a[:]
print(a,b,c)
a.append(6)
print(a,b,c)
del a[0]
print(a,b,c)
