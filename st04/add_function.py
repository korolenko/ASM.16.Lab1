from .student import *
from .monitor import *
def exec_add(typeadd,group):
    try:
        add_actions[typeadd](group)
    except KeyError:
        print("Invalid selection!\n")
        add_actions['add'](group)           
    return

def add(group):
    print("1 for add student")
    print("2 for add monitor")
    typeadd = input(" >>  ")
    exec_add(typeadd,group)
    
    return

def student(group):
    name = input("Enter name >>  ")
    age = input("Enter age >>  ")
    grants = input("Enter grants >>  ")
    address = input("Enter address >>  ")
    student = Student(name, age, grants, address)
    group.add(student)
    return

def monitor(group):
    name = input("Enter name >>  ")
    age = input("Enter age >>  ")
    grants = input("Enter grants >>  ")
    address = input("Enter address >>  ")
    phone = input("Enter phone >>  ")
    email = input("Enter email >>  ")
    monitor = Monitor(name, age, grants, address, phone, email)
    group.add(monitor)
    return

add_actions = {
    'add': add,
    '1': student,
    '2': monitor
}