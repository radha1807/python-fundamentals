def make_multiplier(n):
    def multiplier(x):
        return n*x
    return multiplier

double = make_multiplier(20)
triple = make_multiplier(3)

print(double(5))
print(triple(89))



def env(x):
    def top(n):
        return x+n
    return top

table = env(30)
cup = env(10)


table(21)
table(43)
cup(90)

print(table(43))
print(cup(90))


def tree(x):
    def sub_tree(y):
        return y-x
    return sub_tree

top = tree(24)
top(54)

print(top(54))



















