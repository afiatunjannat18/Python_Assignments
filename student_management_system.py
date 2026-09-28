class Student:
    def __init__(self, name, student_id, email, age, department):
        self.name = name
        self.student_id = student_id
        self.__email = email
        self.age = age
        self.department = department

    # Encapsulation
    def get_email(self):
        return self.__email

    # Method
    def display_info(self):
        print("Name:", self.name)
        print("Student ID:", self.student_id)
        print("Email:", self.__email)
        print("Age:", self.age)
        print("Department:", self.department)

    # *args demonstrates method overloading
    def calculate_result(self, *marks):
        total = sum(marks)
        average = total / len(marks)

        print("Average:", average)

        if average >= 80:
            print("Grade: A+")
        elif average >= 70:
            print("Grade: A")
        elif average >= 60:
            print("Grade: B")
        elif average >= 50:
            print("Grade: C")
        elif average >= 40:
            print("Grade: D")
        else:
            print("Grade: F")

    def get_student_type(self):
        return "Regular Student"


# Inheritance
class UndergraduateStudent(Student):
    def __init__(self, name, student_id, email, age, department, semester):
        super().__init__(name, student_id, email, age, department)
        self.semester = semester

    # Method overriding
    def get_student_type(self):
        return "Undergraduate Student"

    def display_info(self):
        super().display_info()
        print("Semester:", self.semester)
        print("Student Type:", self.get_student_type())


# Inheritance
class GraduateStudent(Student):
    def __init__(
        self,
        name,
        student_id,
        email,
        age,
        department,
        research_topic
    ):
        super().__init__(name, student_id, email, age, department)
        self.research_topic = research_topic

    # Method overriding
    def get_student_type(self):
        return "Graduate Student"

    def display_info(self):
        super().display_info()
        print("Research Topic:", self.research_topic)
        print("Student Type:", self.get_student_type())


# Creating objects
student1 = UndergraduateStudent(
    "Afia",
    "CSE001",
    "afia@gmail.com",
    22,
    "Computer Science",
    8
)

student2 = GraduateStudent(
    "Sara",
    "CSE002",
    "sara@gmail.com",
    25,
    "Computer Science",
    "Artificial Intelligence"
)


# Display information
print("\n--- Undergraduate Student ---")
student1.display_info()

print("\n--- Graduate Student ---")
student2.display_info()


# Calculate results
print("\n--- Undergraduate Result ---")
student1.calculate_result(85, 90, 78, 88)

print("\n--- Graduate Result ---")
student2.calculate_result(90, 92, 87)


# Polymorphism
print("\n--- Polymorphism ---")

students = [student1, student2]

for student in students:
    print(student.get_student_type())