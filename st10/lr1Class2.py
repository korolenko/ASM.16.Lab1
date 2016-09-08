from .lr1Class1 import *

class Cat(feline):
    __kind='Cat'
    __name='None'
    __owner='None'
    def __init__(self,name = 'unnamed',owner='None',age=0,weight=0):
        self.__name=name
        if(age==0 and weight==0):
            self.set_object(True)
        else:     
            self.__age=age
            self.__weight=weight
            self.__owner=owner

    def set_object(self,init=False):
        if(init==True):
            name=input('Input name:')
            self.__name=name
            owner=input('Input owner\'s name:')
            self.__owner=owner
            
        age=input('Input age:')
        weight=input('Input weight:')
        self.__age=age
        self.__weight=weight
        
    def get(self):
        result = [self.__kind, self.__age, self.__weight]
        return result
    def print_object(self):
        print('Cat object:')
        print('Cat\'s name: {}'.format(self.__name))
        print('Owner\'s name: {}'.format(self.__owner))
        print('age: {}'.format(self.__age))
        print('weight: {}'.format(self.__weight))
        print('***************************')
        
    
