class Animal:
    def __init__(self,name):
        self.name=name
    def get_name(self):
        return self.name
    def set_name(self,value):
        self.name=value
    def say(self):
        print(self.name+' is syaing sometheing ')


class Dog(Animal):
    def __new__(cls,name,age):
        print('A new dog.')
        return super().__new__(cls)
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
    def say(self):
        print(self.name+ ' is making sound wang wang wang...')
    def __del__(self):
        print('{} has been deleted'.format(self.name))


class Cat(Animal):
    def __init__(self,name,color):
        super().__init__(name)
        self.color=color

dog=Dog('tom',2)
del dog


