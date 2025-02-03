# Methods

# Types of Methods
# 1. Constructor Method
# 2. Instance Method
# 3. Static Method
# 4. Class Method


class college:
    college_name = "College of Engineering,Tvm"     # Class Varibles
    def __init__(self,name,course,year):        # Constructor Method
        self.name = name                    # Instance Varibles
        self.course = course                # Instance Varibles
        self.year = year                    # Instance Varibles


    def display_details(self):             #  Instance Method
        print(f"Name: {self.name}\nCourse : {self.course}\nYear : {self.year}\nCollege Name : {college.college_name}")

    
    @staticmethod
    def name_lower(name):                   # Static Method
        return name.lower()
    
    @classmethod
    def change_college(cls,new_college):                     # Class Method
        cls.college_name = new_college


amal = college('Amal','AI','2nd')
# amal.display_details()

kiran = college('Kiran','Mechanical','1st')
# kiran.display_details()

college.change_college('TKM College of Engineering')
kiran.display_details()
amal.display_details()
