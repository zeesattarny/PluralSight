students = []

class Student:
   # pass   # keyword in python that just says do nothing
   school_name = "Springfield Elementary"  # class attriute or a static variable

   def __init__(self, name, student_id=332):  # constructor
       self.name = name  # instance attribute
       self.id = student_id   # instance attribute
       students.append(self)

   def __str__(self):   # method override
        return "Student Name: " + self.name

   def get_name_capitlize(self):
       return self.name.capitalize()

   def get_school_name(self):
       return self.school_name  # referring to class attribute in an instnce



class HighSchoolStudent(Student):

    school_name = "Springfield High Shcool"

    def get_school_name(self):
        return "This is a High School Student"
    
    def get__name__capitalize(self):
        original = super().get_name_capitlize()   # executes the parent class and overrides
        return original + " - HS"

james = HighSchoolStudent("james")
print(james.get__name__capitalize())

