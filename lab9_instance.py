'''
lab9
instance
'''

from lab9_class import my_stat

my_cal_instance = my_stat()

print(my_cal_instance.cal_sigma(5,3))
print(my_cal_instance.cal_pi(5,3))
print(my_cal_instance.cal_factorial(5))
print(my_cal_instance.cal_permutation(5,3))

import numpy as np

print(np.math.factorial(999))
print(my_cal_instance.cal_factorial(999))
