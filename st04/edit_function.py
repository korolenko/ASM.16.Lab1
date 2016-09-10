def exec_edit(studnum,group):
    if studnum == '':
        edit(group)
    else:
        try:
            int(studnum)
            group.check(int(studnum)-1)
            name = input("Enter name >>  ")
            age = input("Enter age >>  ")
            grants = input("Enter grants >>  ")
            address = input("Enter address >>  ")
            group.edit(int(studnum)-1, name, age, grants, address)
        except ValueError:
            print("Invalid selection!\n")
            edit(group)
        except IndexError:
            print("Invalid selection!\n")
            edit(group)
    return

def edit(group):
    if len(group) < 1:
        print("List empty\n")
    else:
        print("Choose student to edit \n")
        print(group)
        studnum = input("Enter number >>  ")
        exec_edit(studnum,group)   
    return