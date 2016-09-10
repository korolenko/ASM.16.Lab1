def exec_delete(studnum,group):
    if studnum == '':
        delete(group)
    else:
        try:
            int(studnum)
            group.check(int(studnum)-1)
            group.delete(int(studnum)-1)
        except ValueError:
            print("Invalid selection!\n")
            delete(group)
        except IndexError:
            print("Invalid selection!\n")
            delete(group)
    return

def delete(group):
    if len(group) < 1:
        print("List empty\n")
    else:
        print("Choose student to delete\n")
        print(group)
        studnum = input("Enter number >>  ")
        exec_delete(studnum,group)
    return