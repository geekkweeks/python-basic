names = []


def get_user_choice():
    user_input = input('your choice: ')
    return user_input


def add_new_name():
    user_input = input('Please type your name here: ')
    if validation_name(user_input) and chars_verify(user_input):
        names.append(user_input)
        


def print_names():
    if len(names) > 0:
        for name in names:
            print(str(len(name)))
    else:
        print('list is empty')


def validation_name(input_name):
    if len(input_name) < 5:
        print('Characters less than 5')
        return False
    return True


def remove_name_on_the_list():
    condition = True
    idx = 0
    while condition:
        if len(names) > 0:
            print('ya masuk')
            names.pop(0)
        else:
            condition = False


def chars_verify(input):
    if 'N' in input or 'n' in input:
        return True
    print('There is no n or N in string')
    return False


waiting_for_input = True

while waiting_for_input:
    print('Please choose')
    print('1. Add new name')
    print('2. Print name length of the list')
    print('3. Remove all names on the list')
    print('q. Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        new_name = add_new_name()
    elif user_choice == '2':
        print_names()
    elif user_choice == '3':
        remove_name_on_the_list()
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid, please pick a avalue from the list')
else:
    print('User left the programm')
