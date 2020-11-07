num = 1
name = 'Mike'
is_ok = True

print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))



num = name
print(num, type(num))

num = 1
name = '1'
new_num = int(name)     #型変換
print(new_num, type(new_num))

print('Hi', 'Mike', sep=',', end='\n')



# import math
# result = math.sqrt(25)
# print(result)
# y = math.log2(10)
# print(y)

# print(help(math))


a = 'a'
print(f'a is {a}')

x, y, z = 1, 2, 3
print(f'a is {x}, {y}, {z}')
print(f'a is {z}, {y}, {x}')

name = 'Takashi'
family = 'Kamita'
print(f'My name is {name} {family}. Watashi ha {family} {name}')




