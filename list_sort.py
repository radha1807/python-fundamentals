num = [12,4,34,9,11]
num.sort()
print(num)
#[4, 9, 11, 12, 34]


names = ['annie','sikander','amy','jake']
new_names  =sorted(names)
print(names)
#['annie', 'sikander', 'amy', 'jake']

sensors = [('temp','def',23.1),('pressure','hij',1013),('humidity','abs',60)]
sensors.sort(key=lambda x:x[1])
print(sensors)
#[('humidity', 'abs', 60), ('temp', 'def', 23.1), ('pressure', 'hij', 1013)]

