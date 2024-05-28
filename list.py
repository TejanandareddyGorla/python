v=[1,23,45,32,45,'Teja']
print(v[5])
print(v[-1])
print(v[0:4:2])

v=[1,23,45,32,45,'Teja']
v.append("python")
print(v)
v.extend([5,36,36,46346])
print(v)

v=[1,23,45,1,1,1,1,1,1,1,1,1,1,1,32,45,'Teja']
print(v.count(1))
v.remove(32)
print(v)


v=[1,23,45,1,1,1,1,1,1,1,1,1,1,1,32,45,'Teja']
v.pop(1)
print(v)
v.remove(45)
print(v)
print(v.index(32))
v.insert(0,"abc")


for i in [1,24,1,4,1544,5,'Teja']:
    print(i)