'''
lab7
while loops
'''

#3.1
i = 0

while i <= 5:
    if i != 3:
        print(i)
    else:
        pass
    
    i += 1


#3.2
i = 1
result = 1

while i <= 5:
    result *= i
    i += 1
    
print(result)

#3.3
i = 1
result = 0

while i <= 5:
    result += i
    i += 1

print(result)

#3.4
i = 3
result = 1

while i <= 8:
    result *= i
    i += 1

print(result)

#3.5
i = 1
result1 = 1
result2 = 1

while i <= 8:
    result1 *= i
    i += 1

i = 1
while i <= 3:
    result2 *= i
    i += 1

print(result1 / result2)

#3.6
num_list = [12,32,43,35]

while len(num_list) > 0:
    num_list.remove(num_list[0])

print(num_list)