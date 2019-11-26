class Parent():

    def lastname(self):
        print('Danladi')

class Child(Parent):

    def firstname(self):
        print('fahad')
    def lastname(self):
        print('Al-arab')

F = Child()

F.firstname()
F.lastname()

