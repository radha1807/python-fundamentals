with open('plants.txt' , 'a') as f:
    f.write('photosynthesis\n')
    f.write('oxygen\n')
    f.write('soil\n')
    
    
print('append successfull')
print('===----===')



with open ('plants.txt', 'r') as f:
    for line in f:
        print(line.strip())
        
