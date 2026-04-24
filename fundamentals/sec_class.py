class dog:
    pass

dog1= dog()
dog2= dog()

print(type(dog1))

print(type(dog2))

print(dog1 is dog2)

print('dog1 add: ',id(dog1))
print('dog2 add: ', id(dog2))

print('is add same?: ', id(dog1) == id(dog2))
