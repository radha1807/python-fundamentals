import json

text = '{"name" : "swara kapoor'

try:
    data = json.loads(text)
except:
    pass

print('script continues...data never set!')
print('trying to use data',data)

