class Student:
    def __init__(self, name, age, grants, address):
        self.setName(name)
        self.setAge(age)
        self.setGrants(grants)
        self.setAddress(address)
    def setName(self, inputValue):
        self._name = inputValue
    def setAge(self, inputValue):
        self._age = inputValue
    def setGrants(self, inputValue):
        self._grants = inputValue
    def setAddress(self, inputValue):
        self._address = inputValue
    def getName(self):
        return self._name
    def getAge(self):
        return self._age
    def getGrants(self):
        return self._grants
    def getAddress(self):
        return self._address
    def __str__(self):
        return 'student: ' + self.getName() + ' age: ' + str(self.getAge()) + ' grants: ' + str(self.getGrants()) + ' address: ' + self.getAddress()