class Student:
    def __init__(self):
        
        self.__grade = 0  

   
    def study(self):
        print("Student is studying.")

 
    def get_grade(self):
        return self.__grade

    def set_grade(self, value):
        if 0 <= value <= 100:
            self.__grade = value



class CollegeStudent(Student):
    
    def study(self):
        print("College student is studying programming.")


regular_student = Student()
regular_student.study()

cs_student = CollegeStudent()
cs_student.study()