myset ={1,2,3,4,5}
print(myset)
print(len(myset))
myset1 ={1,2,3,4,5,5,4,3,2,1}
print(myset1)
print(len(myset1))
myset2 ={1.1,2.2,3.3,4.4,5.5}
print(myset2)
myset3 = {'scooby','dooby','doo'}
print(myset3)
myset4 = {1,2,3,'hi','there',1.265,(2,5),('hi','there'), True,False}
print(myset4)
myset5 = set()
print(type(myset5))
myset6 = {'scooby','dooby','dooby','doo',}
for i in myset6:
    print(i)
for i in enumerate(myset6):
    print(i)
for index,value in enumerate(myset6):
    print(index)
    print(value)
print('doo' in myset6)
print('doody' in myset6)
print('dooby' in myset6)
if 'doo' in myset6:
    print('doo is present')
else:
    print('doo is not present')
myset6.add('cartoon')
print(myset6)
myset6.update(['spd','emergency'])
print(myset6)
myset6.remove('cartoon')
print(myset6)
myset6.clear()
print(myset6)
#del (myset2)
myset1 = myset
print(myset1)
myset2 = myset.copy()
print(myset2)
print(id(myset1), id(myset2))
myset.add('cartoon')
print(myset1,myset2)





