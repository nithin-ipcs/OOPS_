# Constructor

# class college:
#     def __init__(self,name,course,year):        # Constructor
#         self.name = name
#         self.course = course
#         self.year = year
#     def display_details(self):
#         print(f"Name: {self.name}\nCourse : {self.course}\nYear : {self.year}")


# amal = college('Amal','AI','2nd')
# amal.display_details()

# Types of Construtor
# 1. Zero Constructor
# 2. One Argument Constructor
# 3. Multiple Argument Constructor
# 4. Default Argument Constructor


# 1. Zero Constructor
# class college:
#     def __init__(self):
#         self.College_name = "College of Engineering,TVM" 
#     def display_details(self,name,course,year):
#         print(f"Name: {name}\nCourse : {course}\nYear : {year}\nCollege Name : {self.College_name}")


# amal = college()
# amal.display_details('Amal','AI','2nd')


# 2. One Argument Constructor

# class college:
#     def __init__(self,college_name):
#         self.College_name = college_name

#     def display_details(self,name,course,year):
#         print(f"Name: {name}\nCourse : {course}\nYear : {year}\nCollege Name : {self.College_name}")


# amal = college("College of Engineering,Tvm")
# amal.display_details('Amal','AI','2nd')

# 3. Multiple Argument Constructor

# class college:
#     def __init__(self,name,course,year,college_name):        # Constructor
#         self.name = name
#         self.course = course
#         self.year = year
#         self.College_name = college_name
#     def display_details(self):
#         print(f"Name: {self.name}\nCourse : {self.course}\nYear : {self.year}\nCollege Name : {self.College_name}")


# amal = college('Amal','AI','2nd',"College of Engineering,Tvm")
# amal.display_details()

# 4. Default Argument Constructor

class college:
    def __init__(self,name,course,year,college_name="College of Engineering,Tvm"):        # Constructor
        self.name = name
        self.course = course
        self.year = year
        self.College_name = college_name
    def display_details(self):
        print(f"Name: {self.name}\nCourse : {self.course}\nYear : {self.year}\nCollege Name : {self.College_name}")


amal = college('Amal','AI','2nd')
# amal.display_details()

kiran = college('Kiran','Mechanical','1st',"TKM College")
kiran.display_details()

