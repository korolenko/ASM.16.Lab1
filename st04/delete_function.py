def exec_delete(studnum,group):
    try:
        int(studnum)
        group.check(int(studnum)-1)
        group.delete(int(studnum)-1)
    except (ValueError, IndexError):
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