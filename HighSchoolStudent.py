from Classes import Student


class HighSchoolStudent(Student):
    school_name = "Springfield High Shcool"

    def get_school_name(self):
        return "This is a High School Student"

    def get__name__capitalize(self):
        original = super().get_name_capitlize()  # executes the parent class and overrides
        return original + " - HS"


james = HighSchoolStudent("james")
print(james.get__name__capitalize())

