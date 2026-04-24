students = [('alice',90), ('bob', 100),('marie',73)]
students.sort(key=lambda x:x[1])
print(students)

#---------------------------------------
def classify(x):
    if x>3:
        return "pos"
    else:
        return "neg"
print (classify(8))

#with lambda same example
classify = lambda x:  "pos" if x>5 else "neg"
print (classify(2))
print (classify(9))

#----------------------------------------


messages = [
    {'role': 'user',      'tokens': 12},
    {'role': 'assistant', 'tokens': 45},
    {'role': 'system',    'tokens': 8},
]

def get_tokens(m):
    return m['tokens']

messages.sort(key=get_tokens)

for m in messages:
    print (m)
    
messages.sort(key=lambda x:x['tokens'], reverse=True)

for x in messages:
    print(x)

