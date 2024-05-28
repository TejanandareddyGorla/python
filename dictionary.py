d={}
print(type(d))

d={1:'abc',22:'Teja','pythonlife':1}
print(d[1])

d={1:'abc',22:'Teja','pythonlife':1}
print(d.get(1))
print(d.keys())
print(d.values())
print(d.items())

for i,j in  {1:'abc',22:'Teja','pythonlife':1}.items():
    print(i,j)
