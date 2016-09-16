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
        
    def read(self):
        print('список университета: ')
        for Object in self.spisok:
           print(Object)
           
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
