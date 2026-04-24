""" from pathlib import Path

base = Path('data')
full = base/'documents'/'readme.txt'

print(full)
print(full.name)
print(full.parent)
print(str(full))  """


#=========---------==========

from pathlib import Path

p = Path ('plants.txt')

p.write_text('hello from here', encoding = 'utf-8')
content = p.read_text(encoding = 'utf-8')

print(content)
print(type(content))