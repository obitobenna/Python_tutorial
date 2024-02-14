#school management system
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.enrollments = []

    def enroll(self, course):
        self.enrollments.append(course)
        course.add_student(self)

    def get_courses(self):
        return [course.name for course in self.enrollments]


class Teacher:
    def __init__(self, name, teacher_id):
        self.name = name
        self.teacher_id = teacher_id
        self.courses = []

    def assign_to_course(self, course):
        self.courses.append(course)
        course.set_teacher(self)


class Course:
    def __init__(self, name, course_id):
        self.name = name
        self.course_id = course_id
        self.students = []
        self.teacher = None

    def add_student(self, student):
        self.students.append(student)

    def set_teacher(self, teacher):
        self.teacher = teacher

    def get_student_list(self):
        return [student.name for student in self.students]


class Enrollment:
    def __init__(self, student, course):
        self.student = student
        self.course = course

    def enroll(self):
        self.student.enroll(self.course)


# Example usage
if __name__ == "__main__":
    # Creating some students
    alice = Student("Alice", "S001")
    bob = Student("Bob", "S002")

    # Creating a teacher
    mr_smith = Teacher("Mr. Smith", "T001")

    # Creating courses
    math = Course("Mathematics", "C001")
    science = Course("Science", "C002")

    # Assigning teacher to courses
    mr_smith.assign_to_course(math)
    mr_smith.assign_to_course(science)

    # Enrolling students in courses
    alice.enroll(math)
    bob.enroll(science)

    # Printing enrolled courses for Alice
    print(f"Alice's Courses: {alice.get_courses()}")

    # Printing students in Mathematics course
    print(f"Students in Mathematics: {math.get_student_list()}")



    
