students = [('alice',90), ('bob', 100),('marie',73)]
students.sort(key=lambda x:x[1])
print(students)


def classify(x):
    if x>3:
        return "pos"
    else:
        return "neg"
print (classify(8))


classify = lambda x:  "pos" if x>5 else "neg"
print (classify(2))
print (classify(9))