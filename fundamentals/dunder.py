class chat:
    def __init__(self,role,content,tokens=0):
        self.role = role
        self.content = content
        self.tokens = tokens
        
    def __str__(self) -> str:
        preview = self.content[:50] + '...' if len(self.content) > 50 else self.content
        return f'[{self.role.upper()}] {preview}'

msg = chat('user', 'what is rag?', tokens=12)
msg_long = chat('assist', 'rag stands for retrieval augmented gen and it fetches relvant docs first')

print(msg)
print(msg_long)
print(f"message: {msg}")

'''msg = chat('user','whats rag in one sentence?', tokens=12)

print(msg)
print(repr(msg))'''

    #A class with no __str__ or __repr__
    #output
    #<__main__.chat object at 0x0000022D3CC46F90>
    #<__main__.chat object at 0x0000022D3CC46F90>


   