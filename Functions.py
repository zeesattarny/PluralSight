students= []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase

def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_students(name, student_id=332):
    student = {"name": name, "student_id": student_id}
    students.append(student)

def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not write student in file")

def read_file():
    try:
        f = open("students.txt","r")
        for student in f.readlines():
            add_students(student)
        f.close()
    except Exception:
        print("Could not read file")


# def var_args(name, *args):
#     print(name)
#     print(*args)
#
# def var_kwargs(name, **kwargs):
#     print(name)
#     print(kwargs["description"], kwargs["feedback"])
#

#add_students(name="Mark", student_id=3235)

#var_args("Jogn", "whta", "are", "you", "doing")

#var_kwargs(name="Kevin", description="learning Python", feedback= None, pluralSiteSubscriber = True)


read_file()
print_students_titlecase()

student_name = input("Enter student name: ")
student_id = input("Enter student ID: ")
add_students(student_name, student_id)
save_file(student_name)