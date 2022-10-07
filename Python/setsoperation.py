a={1,2,3,4,5}
b={3,4,5,6,7,8,9,10}
c={8,9,10,11,12}
#union
print(a | b)
print(a.union(b))
print(a.union(b,c))
#intersection
print(a&b)
print(a.intersection(b))
#difference
print(a.difference(b))
print(b.difference(a))
#symmetric difference
print(a^b)
print(a.symmetric_difference(b))
#subset,superset,disjoint
print(b.issubset(a))
print(a.issuperset(b))
print(c.isdisjoint(a))
