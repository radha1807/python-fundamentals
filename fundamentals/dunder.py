class chat:
    def __init__(self,role,content,tokens=0):
        self.role = role
        self.content = content
        self.tokens = tokens
        
msg = chat('user','whats rag in one sentence?', tokens=12)

print(msg)
print(repr(msg))

#A class with no __str__ or __repr__
#output
#<__main__.chat object at 0x0000022D3CC46F90>
#<__main__.chat object at 0x0000022D3CC46F90>