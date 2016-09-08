import pickle
from st10.lr1Class1 import *
from st10.lr1Class2 import *

class feline_list():
    __container=[]

    def __init__(self,data=[]):
        self.__container=data

    def fadd(self,ttype=0):
        elem=None
        if(ttype==1):
            elem = Cat('','',1,1)
        else:
            elem = feline('',0,0)
        elem.set_object(True);    
        self.__container.append(elem)

    def fclear(self):
        self.__container.clear()

    def fshow(self):
        for elem in self.__container:
            elem.print_object()
            
    def fdel(self,index=0):
        self.__container.pop(index)
        print('The chosen object was deleted.')

    def fread(self,filename='data.txt'):
        with open(filename,'rb') as file:
            self.__container = pickle.load(file)
        print('The data was read.')
        
    def fwrite(self,filename='data.txt'):
        with open(filename,'wb') as file:
            pickle.dump(self.__container,file)
        print('The data was written.')

    def flen(self):
        return len(self.__container)
    
    def fedit(self,index,ttype=0):
        elem=self.__container.pop(index)
        elem.set_object(True);
        self.__container.insert(index,elem)

    
