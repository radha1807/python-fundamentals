class dog:
    def __init__(self,name ,breed):
        self.name = name
        self.breed = breed 

dog1 = dog('rex', 'labrador')
dog2 = dog('bella', 'poodle')

print(dog1.name, dog1.breed)
print(dog2.name, dog2.breed)  

dog1.name = 'max'
print('after rename - dog1: ',dog1.name, '| dog2: ',dog2.name)  
   