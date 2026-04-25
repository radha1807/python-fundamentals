a = [1,2,3,4,6]
b = [1,2,3,4,6]

print('a == b: ', a ==b)
print('a is b:', a is b)

print()

c = a
print('a is c:' , a is c)
c.append(4)
print('a after c.append(4):', a)
print()
