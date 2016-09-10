from .monitor import *
import pickle
class Group:
    def __init__(self):
        self._student = []
    def add(self, x):
        self._student.append(x)
    def edit(self, num, name, age, grants, address):
        self._student[num].setName(name)
        self._student[num].setAge(age)
        self._student[num].setGrants(grants)
        self._student[num].setAddress(address)
        if type(self._student[num]) == type(Monitor(1,2,3,4,5,6)):
            phone = input("Enter phone >>  ")
            email = input("Enter email >>  ")
            self._student[num].setPhone(phone)
            self._student[num].setEmail(email)
    def delete(self,num):
        self._student.pop(num)
    def clear(self):
        self._student = []
    def check(self,num):
        return self._student[num].getName()
    def load(self):
        self._student = pickle.load( open( "st04/04.p", "rb" ) )
    def save(self):
        pickle.dump( self._student, open( "st04/04.p", "wb" ) )
    def __len__(self):
        return len(self._student)
    def __str__(self):
        tmp_list = []
        count = 1
        if self._student == []:
            tmp_string="Empty list\n"
        else:
            for e in self._student:
                tmp_list.append(str(count) +". " + str(e))
                count +=  1
            tmp_string = "\n".join(tmp_list)
        return tmp_string