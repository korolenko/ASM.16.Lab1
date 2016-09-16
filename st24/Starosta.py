from .Student import *
class Starosta(Student):
    def __init__(self,age=22,salary=1000):
        super().__init__()
        self.age=age
        self.salary=salary
        
    def write_S(self):
        self.name=input('введите имя старосты:')
        self.group=input('введите группу старосты:')
        self.mark=input('введите средний балл старосты:')
        self.age=input('введите возраст старосты:')
        self.salary=input('введите зарплату старосты')
        
    def __str__(self):
        return '[Староста: %s,%s,%s,%s,%s]' %(self.name, self.group,self.mark,self.age,self.salary)    

