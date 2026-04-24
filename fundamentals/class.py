import os

with open ('school.txt', 'w') as f:
    f.write('students\n')
    f.write('teachers\n')
    f.write('principle\n')
    
print('write done')

with open('school.txt', 'r') as f:
    content = f.read()
    print('file contents:')
    print(content)
    
print('file size in bytes: ', os.path.getsize('school.txt'))