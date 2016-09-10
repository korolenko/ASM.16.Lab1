from .group import *
from .add_function import *
from .clear_function import *
from .delete_function import *
from .edit_function import *
from .exit_function import *
from .load_function import *
from .print_function import *
from .save_function import *

group = Group()

def main():    
    print("Menu")
    print("1. Add object")
    print("2. Edit object")
    print("3. Delete object")
    print("4. Print list")
    print("5. Save")
    print("6. Load")
    print("7. Clear")
    print("0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)

 
def exec_menu(choice):
    try:
        menu_actions[choice](group)
    except KeyError:
        print("Invalid selection!\n")
    menu_actions['main']()


menu_actions = {
    'main': main,
    '1': add,
    '2': edit,
    '3': delete,
    '4': print_list,
    '5': save,
    '6': load,
    '7': clear,
    '0': exit,
}
 
if __name__ == "__main__":
    main()