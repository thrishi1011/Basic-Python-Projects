# Decorators in Python
def add_sprinkles(func):
    def wrapper():
        print('you added sprinkles')
        func()
    return wrapper

def add_fudge(func):
    def wrapper():
        print('you added fudge')
        func()
    return wrapper

def get_ice_cream(func):
    def wrapper():
        print('here is your icecream')
        func()
    return wrapper

@add_sprinkles
@add_fudge
@get_ice_cream
def cone():
    print('here is your cone')

cone()

# --------------
# Decorators with arguments

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print('you added sprinkles')
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print('you added fudge')
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream")


get_ice_cream("Butter_Scoth")

# ---------------
# File handling in Python

import os

file_plath = "name of the file"

if os.path.exists(file_plath):
    print(f'The location of the {file_plath} exists')

    if os.path.isfile(file_plath):
        print('That is a file')
    elif os.path.isdir(file_plath):
        print('That is a directory')

else:
    print('The file does not exist')

# ---------------
# writing to a file(.txt)

empoyees = ['John', 'Jane', 'Doe']
file_plath = "write the location of the file"
with open(file_plath, 'w') as file:
    for employee in empoyees:
        file.write(employee + '\n')
    print(f'txt file created at {file_plath}')

# ---------------
# writing to a file(.json)

import json
employees = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}
file_plath = "write the location of the file"
with open(file_plath, 'w') as file:
    json.dump(employees, file, indent=4)
    print(f'json file created at {file_plath}')

# ---------------
# writing from a file(.csv)

import csv
employees = [
    ['name', 'age', 'city'],
    ['John', 30, 'New York'],
    ['Jane', 25, 'Los Angeles'],
    ['Doe', 22, 'Chicago']]

file_plath = "write the location of the file"
with open(file_plath, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(employees)
    print(f'csv file created at {file_plath}')

# ---------------

