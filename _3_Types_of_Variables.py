# Varibles

# Types of Variables
# 1. Local Varible
# 2. Global Variable
# 3. Instance Varible
# 4. Class/Static Varible



class college:
    college_name = "College of Engineering,Tvm"     # Class Varibles
    def __init__(self,name,course,year):        # Constructor
        self.name = name                    # Instance Varibles
        self.course = course                # Instance Varibles
        self.year = year                    # Instance Varibles
    def display_details(self):
        print(f"Name: {self.name}\nCourse : {self.course}\nYear : {self.year}\nCollege Name : {college.college_name}")


amal = college('Amal','AI','2nd')
# amal.display_details()

kiran = college('Kiran','Mechanical','1st')
# kiran.display_details()

print(college.college_name)

print()
