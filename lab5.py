'''
lab5
if statements
'''

#3.1
alien_color = 'green'

if alien_color == 'green':
    print('you got 5 points')

#3.2
if alien_color == 'green':
    print('you got 5 points')
else:
    print('you got 10 points')

#3.3
favorite_fruits = ['grape', 'strawberry', 'apple']

if 'grape' in favorite_fruits:
    print('you really like grapes!')

if 'strawberry' in favorite_fruits:
    print('you really like strawberries!')

if 'apple' in favorite_fruits:
    print('you really like apples!')

#3.4
age = 21

if age < 10:
    print("you're a kid")

elif age < 20:
    print("you're a teenager")

else:
    print("you're an adult")
    if age >= 65:
        print("you're an elder")
