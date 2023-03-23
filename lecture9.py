'''
lacture 9
define class
'''

class car:
    maker = 'toyota'
    
    def report_maker(self):
        
        return self.maker
    
    def __init__(self,input_model):
        self.model = input_model
    
    def report(self):
        return self.maker, self.model
    
my_car_instance = car('highlander')
print(my_car_instance.maker)
print(my_car_instance.model)

my_highlander = car('highlander')
print(my_highlander.maker)
print(my_highlander.model)
print(my_highlander.report())
