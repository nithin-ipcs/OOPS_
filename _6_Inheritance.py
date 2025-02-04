# Inheritance
# class dad:  # Parent class
#     def flat(self):
#         print("3bhk")
#     def car(self):
#         print("BMW")

# class son(dad):        # Child Class
#     def bike(self):
#         print("Honda")
#     def phone(self):
#         print("Iphone")

# son_obj = son()
# son_obj.bike()
# son_obj.phone()
# son_obj.flat()
# son_obj.car()

# Types of Inheritance
# 1. Single Inheritance
# 2. Multilevel Inheritance
# 3. Multiple Inheritance
# 4. Hierarchical Inheritance
# 5. Hybrid Inheritance

# 1. Single Inheritance

# class dad:  # Parent class
#     def flat(self):
#         print("3bhk")
#     def car(self):
#         print("BMW")

# class son(dad):        # Child Class
#     def bike(self):
#         print("Honda")
#     def phone(self):
#         print("Iphone")


# 2. Multilevel Inheritance

class dad:  # Parent class
    def flat(self):
        print("3bhk")
    def car(self):
        print("BMW")

class mom(dad):
    def scooty(self):
        print('Activa')
    def Jewelery(self):
        print("Gold")

class son(mom):        # Child Class
    def bike(self):
        print("Honda")
    def phone(self):
        print("Iphone")
    def car(self):
        print("Benz")


# son1_obj = son()
# son1_obj.bike()
# son1_obj.Jewelery()
# son1_obj.car()


# 3. Multiple Inheritance

class dad:  # Parent class
    def flat(self):
        print("3bhk")
    def car(self):
        print("BMW")

class mom:   # Parent class
    def scooty(self):
        print('Activa')
    def Jewelery(self):
        print("Gold")

class son(dad,mom):        # Child Class
    def bike(self):
        print("Honda")
    def phone(self):
        print("Iphone")
    def car(self):
        print("Benz")

son1_obj = son()
son1_obj.bike()
son1_obj.Jewelery()
son1_obj.car()

# 4. Hierarchical Inheritance

class dad:  # Parent class
    def flat(self):
        print("3bhk")
    def car(self):
        print("BMW")

class mom(dad):   # Parent class
    def scooty(self):
        print('Activa')
    def Jewelery(self):
        print("Gold")

class son(dad):        # Child Class
    def bike(self):
        print("Honda")
    def phone(self):
        print("Iphone")
    def car(self):
        print("Benz")

class daughter(dad):
    def phone(self):
        print("Samsung")
    def scooty(self):
        print('Tvs')



# 5. Hybrid Inheritance

class dad:  # Parent class
    def flat(self):
        print("3bhk")
    def car(self):
        print("BMW")

class mom(dad):   # Parent class
    def scooty(self):
        print('Activa')
    def Jewelery(self):
        print("Gold")

class son(mom):        # Child Class
    def bike(self):
        print("Honda")
    def phone(self):
        print("Iphone")
    def car(self):
        print("Benz")

class daughter(mom):
    def phone(self):
        print("Samsung")
    def scooty(self):
        print('Tvs')

class son_frd(son):
    def phone(self):
        print("One plus")