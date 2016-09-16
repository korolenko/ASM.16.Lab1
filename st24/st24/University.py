import pickle
from .Student import *
from .Starosta import * 
class University:
    def __init__(self,spisok=[]):
        self.spisok=spisok

    def new_stu(self):
        student=Student()
        student.write()
        self.spisok.append(student)
        
    def new_sta(self):
        starosta=Starosta()
        starosta.write_S()
        self.spisok.append(starosta)
        
    def change(self):
        self.read()
        num=input('введите номер объекта: ')
        if type (self.spisok[int(num)])== Student:
            student=Student()
            student.name=input('введите имя студента:')
            student.group=input('введите группу студента:')
            student.mark=input('введите средний балл студента:')
            self.spisok[int(num)]=student
        else:
            starosta=Starosta()
            starosta.name=input('введите имя старосты:')
            starosta.group=input('введите группу старосты:')
            starosta.mark=input('введите средний балл старосты:')
            starosta.age=input('введите возраст старосты:')
            starosta.salary=input('введите зарплату старосты')
            self.spisok[int(num)]=starosta
        
    def read(self):
        print('список университета: ')
        for Number,Object in enumerate(self.spisok):
           print (Number, Object) 
           
    def clear(self):
        self.spisok.clear()
        print('список чист')
        
    def write_f(self):
        pickle.dump(self.spisok, open('file.dat', 'wb'))
        print('запись в файл произведена')
        
    def read_f(self):
        group=pickle.load(open('file.dat', 'rb'))
        for a in group:
            self.spisok.append(a)
        print('данные из файла считаны')
