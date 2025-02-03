
# Creating  a class
class fruit:
    def __init__(self, name, color, taste):
        self.name = name
        self.color = color
        self.taste = taste

    def Color(self):
        print(f"{self.name} is {self.color} in color")

    def Taste(self):
        print(f"{self.name} tastes like {self.taste}")


# Creating different object form same class
apple = fruit('Apple','Red','Sweet')
banana = fruit('Banana','Yellow','Sweet')
apple.Color()
banana.Color()

lst = list((3,4,5,))
lst.append(8)
print(type(lst))
print(type(apple))


# Properties of OOPS Concept
# 1.Constructor
# 2.Encapsulation
# 3.Inheritance
# 4.Abstraction
# 5.Polymorphism