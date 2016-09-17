class Student:
    def __init__(self, name='Student', group='AA-00-0', mark=5.0):
        self.name=name
        self.group=group
        self.mark=mark
        
    def write(self):
        self.name=input('введите имя студента:')
        self.group=input('введите группу студента:')
        self.mark=input('введите средний балл студента:')
        
    def __str__(self):
        return 'Студент: %s,%s,%s' %(self.name, self.group,self.mark)

