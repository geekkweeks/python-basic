name = 'Alfan'
age = 10


def get_user_name_and_age():
    global name
    global age
    name = input('Please enter your name ')
    age = int(input('Please enter your age '))

def print_two_arguments(your_address, your_salary):
    print('Your address is ' + your_address + ' and your salary  is $' + str(your_salary))

def get_decade_of_age():
    print('Your age in decade is ' + str(age % 10 ))

get_user_name_and_age()

print('Your name is ' + name + ' and your age is ' + str(age))
print_two_arguments('Jalan kebagusan raya', 55000.45)
get_decade_of_age()