from st10.lr1Class1 import *
from st10.lr1Class2 import *
from st10.lr1Container import *

object_list=feline_list()

def action_add():
    def add_elem():
        print('0-feline\n1-cat')
        ttype=ord(input(''))-ord('0')
        if(ttype==0 or ttype==1):
            object_list.fadd(ttype)
        else:
            print('error type')
    return add_elem

def action_del():
    def del_elem():
        index=ord(input('enter index:'))-ord('0')
        if(object_list.flen()<=index or index<0):
            print('Wrong index: {}'.format(index))
        else:       
            object_list.fdel(index)
    return del_elem

def action_show():
    def show_list():
        object_list.fshow()
    return show_list

def action_edit():
    def edit_elem():
        index=ord(input('enter index:'))-ord('0')
        if(object_list.flen()<=index or index<0):
            print('Wrong index: {}'.format(index))
        else:       
            object_list.fedit(index)
    return edit_elem

def action_write():
    def write_list():
        filename=input('Enter filename: ')
        if(len(filename)<3):
            object_list.fwrite()
        else:
            object_list.fwrite(filename)
    return write_list
    
def action_read():
    def read_list():
        filename=input('Enter filename: ')
        if(len(filename)<3):
            object_list.fread()
        else:
            object_list.fread(filename)
    return read_list

def action_clear():
    def clear_list():
        object_list.fclear()
    return clear_list

def init(menu,actions):
    menu.append(action_add())
    actions.append('Add')
    menu.append(action_edit())
    actions.append('Edit')
    menu.append(action_del())
    actions.append('Delete')
    menu.append(action_show())
    actions.append('Show list')
    menu.append(action_clear())
    actions.append('Clear list')
    menu.append(action_write())
    actions.append('Write list to file')
    menu.append(action_read())
    actions.append('Read list from file')
    
def main():
    menu=[]
    actions=[]
    init(menu,actions)
    
    while(True):
        print('Choose action(any other to exit):')
        for i in range(len(menu)):
            print('{index}: {name}'.format(index=i, name=actions[i]))
        command=ord(input(''))-ord('0')
        if (command<len(menu) and command>-1):
            menu[command]()  
        else:
            break     
    
if __name__=='__main__':
    main()

