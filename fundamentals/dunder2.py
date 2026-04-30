class chat:
    def __init__(self,role,content,tokens=0):
       self.role = role
       self.content = content
       self.tokens = tokens 
       
#msg = chat('user', 'what is rag?')
#len(msg)

    def __len__(self) -> int:
        return len(self.content)
    
msg_short = chat('user',      'Hi')
msg_long  = chat('assistant', 'RAG stands for retrieval augmented generation')

print(len(msg_short))    # 2   ← len("Hi")
print(len(msg_long))   

messages = [msg_long , msg_short]  
messages.sort(key=lambda m: len(m))

lambda m: len(m)

def get_length(m):
    return len(m)

messages.sort(key=get_length)

for m in messages:
    print(f"  len={len(m):3d} | {m.content[:40]}")