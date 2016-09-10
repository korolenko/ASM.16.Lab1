from st10.lr1Class1 import *
from st10.lr1Class2 import *
from st10.lr1Container import *

object_list=feline_list()

def add_elem():
    print('0-feline\n1-cat')
    ttype=ord(input(''))-ord('0')
    if(ttype==0 or ttype==1):
        object_list.fadd(ttype)
    else:
        print('error type')

def del_elem():
    index=ord(input('enter index:'))-ord('0')
    if(object_list.flen()<=index or index<0):
        print('Wrong index: {}'.format(index))
    else:       
        object_list.fdel(index)

def edit_elem():
    index=ord(input('enter index:'))-ord('0')
    if(object_list.flen()<=index or index<0):
        print('Wrong index: {}'.format(index))
    else:       
        object_list.fedit(index)

def write_list():
    filename=input('Enter filename: ')
    if(len(filename)<3):
        object_list.fwrite()
    else:
        object_list.fwrite(filename)
    
def read_list():
    filename=input('Enter filename: ')
    if(len(filename)<3):
        object_list.fread()
    else:
        object_list.fread(filename)

def init(menu,actions):
    menu.append(add_elem)
    actions.append('Add')
    menu.append(edit_elem)
    actions.append('Edit')
    menu.append(del_elem)
    actions.append('Delete')
    menu.append(object_list.fshow)
    actions.append('Show list')
    menu.append(object_list.fclear)
    actions.append('Clear list')
    menu.append(write_list)
    actions.append('Write list to file')
    menu.append(read_list)
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

