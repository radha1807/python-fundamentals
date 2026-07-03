class planets:
    def __init__(self,name,position):
        self.name = name 
        self.position = position
        
x = planets('earth', 3)
x.position = 4

print('the name and position of planet is: ', x.position,x.name)