class chat:
    def __init__(self,role,content,tokens=0):
        self.role = role
        self.content = content
        self.tokens = tokens
        
msg = chat('user','whats rag in one sentence?', tokens=12)

print(msg)
print(repr(msg))


