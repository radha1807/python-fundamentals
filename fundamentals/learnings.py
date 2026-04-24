with open('diary.txt' , 'w') as f:
    f.write('learned file i/o\n')
    f.write('practiced questions\n')
    f.write('learned functions and lambda\n')
    
print('file created')

with open('diary.txt', 'r') as f:
    content = f.read()
    print('file content:: ')
    print(content)
    
with open('diary.txt' , 'a') as f:
    f.write('misc questions done')


print('list of things done:')
with open('diary.txt', 'r')as f:
    for line in f:
        print(line.strip())