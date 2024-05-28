c=()
print(type(c))

c=(1,24,1,3,14,14,'Teja')
print(c[-1])
print(c[0:4:2])

c=(1,24,1,3,14,14)
print(min(c))
print(max(c))
print(len(c))

t1=(1,2,3)
t2=(4,5,6)
print(t1+t2)

c=(1,24,1,3,14,14)
print(c*22)

for i in c:
    print(i)

print(1 in c)
print(11 not in c)