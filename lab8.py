'''
lab8
functions
'''

#3.1
def count(string):
    words = string.split(' ')
    print(len(words))

#3.2
count('hello world!')

#3.3
#input_list = [1,2,3]

def min_val(input_list):
    
    possible_result = input_list[0]
    
    for num in input_list:
        if type(num) is not str:
            if possible_result > num:
                possible_result = num
    return(possible_result)

#3.4
demo_list = [1,2,3,4,5,6]

print(min_val(demo_list))

#3.5
mix_list = [1,2,3,4,'a',5,6]

min_val(mix_list)
