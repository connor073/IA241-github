'''
function
'''

def cal_plus(input1,input2):
    return input1 + input2
    
print(cal_plus(1,3))
print(cal_plus(2,7))




def sigma(n,m):
    result = 0
    for i in range(n,m+1):
        result = result + i
    return result
print(sigma(3,5))