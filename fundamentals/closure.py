#===================eg 1==========================

def make_multiplier(n):
    def multiplier(x):
        return n*x
    return multiplier

double = make_multiplier(20)
triple = make_multiplier(3)

print(double(5))
print(triple(89))

#===================eg 2===========================

def env(x):
    def top(n):
        return x+n
    return top

table = env(30) #python creates temp space x=30
cup = env(10)

 
table(21) #top(21) n = 21   calculation: 30+21 
table(43)
cup(90)

print(table(21))
print(cup(90))


#==================eg 3========================

def tree(x):
    def sub_tree(y):
        return y-x
    return sub_tree

top = tree(24)
top(54)

print(top(54))

#===================eg 4=======================

def greeting(a):
    def greeter(x):
        return a+x
    return greeter

house = greeting('good morning ')
house('radha')

print(house('radha'))












