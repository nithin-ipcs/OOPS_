# Encapsulation

class college:
    college_name = "College of Engineering,Tvm"     # Class Varibles
    def __init__(self,name,course,year,user_id,pswd):        # Constructor Method
        self.name = name                    # Instance Varibles
        self.course = course                # Instance Varibles
        self.year = year                    # Instance Varibles
        self.user_id = user_id
        self.__psd = pswd                   # Private Members 


    def display_details(self):             #  Instance Method
        print(f"Name: {self.name}\nCourse : {self.course}\nYear : {self.year}\nCollege Name : {college.college_name}")

    
    @staticmethod
    def name_lower(name):                   # Static Method
        return name.lower()
    
    @classmethod
    def change_college(cls,new_college):                     # Class Method
        cls.college_name = new_college

    def view_psd(self):                      # Public
        return self.__psd
    
    def set_psd(self,new_psd):
        self.__psd =  new_psd

ammu = college('Ammu','BTech','2nd','ammu112','ammu@123')
ammu.set_psd('ammu@888')
print(ammu.view_psd())