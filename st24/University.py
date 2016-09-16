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
        if len(self.spisok)==0:
            print('список пуст!')
        else:
            self.read()
            num=input('введите номер объекта: ')
            if int(num)<0 or int(num)>len(self.spisok):
                print('неверный номер!')
            else:
                if type (self.spisok[int(num)])== Student:
                    student=Student()
                    student.write()
                    self.spisok[int(num)]=student
                else:
                    starosta=Starosta()
                    starosta.write_S()
                    self.spisok[int(num)]=starosta
                print('объект изменен!')
        
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
