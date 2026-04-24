#----------------------------------------------
nums = [4,5,6,2,9]
doubled = list(map(lambda x: x*2,nums))
print(doubled)


points = [11,22,33,44]
config = [x*3 for x in points]
print(points)

#---------------------------------------------

#example 2 c=>f

#using lambda
cel = [0,14,45,98]
far = list(map(lambda x: (x*9/5) + 32, cel))
print(far)

#using list comprehension
cel = [83,72,1,34]
far = [(c * 9/5) + 32 for c in cel]
print('the conversion of cel',cel,'to far is: ',far)



messages = [
    {'role': 'user',      'content': 'What is RAG?'},
    {'role': 'assistant', 'content': 'RAG is retrieval augmented generation'},
]
content = list(map(lambda x: x['content'],messages))
print(content)

content = [x['content'] for x in messages]
print(content)


text = ['ravi', 'jiya','anu']
classes = list(map(str.strip,text))
print(classes)

classes = list(map(lambda x: x.strip(), text))
print(classes)

cleaned_and_reversed = [s.strip()[-1::] for s in text]
print(cleaned_and_reversed)