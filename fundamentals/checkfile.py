from pathlib import Path

#creating file first so it exists

p = Path('abc.txt')
p.write_text('some content',encoding = 'utf-8')

#check properties

print('exists ',p.exists())  
print('is file?', p.is_file()) 
print('is dir?', p.is_dir())

#only read if exists

if p.exists():
    print('reading: ', p.read_text(encoding = 'utf-8'))
else:
    print('file not found')
    
#check path that does not exists

missing = Path('ghost.txt')
print('missing exists?', missing.exists())