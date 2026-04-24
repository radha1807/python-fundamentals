from pathlib import Path

p = Path ('xyz.txt')
p.write_text ('there are 26 alphabetes', encoding = 'utf-8')

print('exists: ', p.exists())
print('is file?: ', p.is_file())
print('is dir: ', p.is_dir())

if p.exists():
    print('file exist, reading',p.read_text(encoding = 'utf-8'))
else:
    print('not found')
    

