class feline:
    __kind='None'
    __age=0
    __weight=0
    def __init__(self,kind='None',age=0,weight=0):
        if(kind=='None' and age==0 and weight==0):
            self.set_object()
        else:     
            self.__kind=kind
            self.__age=age
            self.__weight=weight

    def set_object(self,init=False):
        if(init==True):
            kind=input('Input kind:')
            self.__kind=kind
        age=input('Input age:')
        weight=input('Input weight:')
        self.__age=age
        self.__weight=weight
        
    def get(self):
        result = [self.__kind, self.__age, self.__weight]
        return result
    def print_object(self):
        print('Feline object:')
        print('kind: '+self.__kind)
        print('age: {}'.format(self.__age))
        print('weight: {}'.format(self.__weight))
        print('============================')
    
