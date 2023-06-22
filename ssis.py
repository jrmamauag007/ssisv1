import json
class Student:
    def __init__(self, id, name, course):
        self.id = id
        self.name = name
        self.course = course

class Course:
    def __init__(self, code, name):
        self.code = code
        self.name = name

class SimpleStudentInformationSystem:
    def __init__(self,students_file,courses_file):
        self.students_file = students_file
        self.courses_file = courses_file
        self.load_students()
        self.load_courses()


    def print_menu(self):
        print("\nWelcome to my Simple Student Information System!\n")
        print("1. Add Student")
        print("2. Add Course")
        print("3. List Students")
        print("4. List Courses")
        print("5. Search Student")
        print("6. Edit Student")
        print("7. Edit Course")
        print("8. Delete Student")
        print("9. Delete Course")
        print("0. Exit")

    def run(self):
        while True:
            self.print_menu()
            choice = input("Enter your choice (0-9): ")
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.add_course()
            elif choice == "3":
                self.list_students()
            elif choice == "4":
                self.list_courses()
            elif choice == "5":
                self.search_student()
            elif choice == "6":
                self.edit_student()
            elif choice == "7":
                self.edit_course()
            elif choice == "8":
                self.delete_student()
            elif choice == "9":
                self.delete_course()
            elif choice == "0":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

############################################################################################################

    def load_students(self):
        try:
            with open(self.students_file, "r") as f:
                lines = f.readlines()
                self.students = []
                for line in lines:
                    parts = line.strip().split(",")
                    student = Student(parts[0], parts[1], parts[2])
                    self.students.append(student)
        except FileNotFoundError:
            with open(self.students_file, "w") as f:
                f.write("")
            self.students = []

    def load_courses(self):
        try:
            with open(self.courses_file, "r") as f:
                lines = f.readlines()
                self.courses = []
                for line in lines:
                    parts = line.strip().split(",")
                    code = parts[0]
                    name = parts[1]
                    course = Course(code, name)
                    self.courses.append(course)
        except FileNotFoundError:
            with open(self.courses_file, "w") as f:
                f.write("")
            self.courses = []

    def save_students(self):
        with open(self.students_file, "w") as f:
            for student in self.students:
                    f.write(f"{student.id},{student.name},{student.course}\n")

    def save_courses(self):
        with open(self.courses_file, "w") as f:
            for course in self.courses:
                f.write(f"{course.code},{course.name}\n")



############################################################################################################

    def add_course(self):
        code = input("Enter course code: ")
        # Check if course code already exists
        for course in self.courses:
            if course.code == code:
                print("Course code already exists.")
                return
        if not code:
            print("Invalid input. Course code cannot be blank.")
            return
        name = input("Enter course name: ")
        if not name:
            print("Invalid input. Course name cannot be blank.")
            return
        course = Course(code, name)
        self.courses.append(course)
        self.save_courses()
        print("Course added successfully.")

    def add_student(self):
        id = input("Enter student ID: ")
        # Check if student ID already exists
        for student in self.students:
            if student.id == id:
                print("Student ID already exists.")
                return
        if not id:
            print("Invalid input. Student ID cannot be blank.")
            return

        name = input("Enter student name: ")
        if not name: 
            print("Invalid input. Name cannot be blank.")
            return
        
        course_code = input("Enter course code: ")
        if not course_code:
            print("Invalid input. Course code cannot be blank.")
            return
        if course_code not in [course.code for course in self.courses]:
            print("Course not found. Here are the available courses:")
            self.list_courses()
            return
        
        student = Student(id, name, course_code)
        self.students.append(student)
        self.save_students()
        print("Student added successfully.")

############################################################################################################

    def delete_student(self):
        id = input("Enter student ID to delete: ")
        for student in self.students:
            if student.id == id:
                self.students.remove(student)
                self.save_students()
                print("Student deleted successfully.")
                return
        print("Student not found.")

    def delete_course(self):
        code = input("Enter course code to delete: ")
        for course in self.courses:
            if course.code == code:
                self.courses.remove(course)
                self.save_courses()
                print(f"Course {code} deleted successfully.")
                return
        print(f"Course {code} not found.")

############################################################################################################

    def edit_student(self):
        search = input("Enter search term (Name or ID): ")
        
        if self.students:
            for student in self.students:
                if search in student.id or search in student.name:
                    print(f"ID: {student.id}, Name: {student.name}, Course: {student.course}")

                    choice = input("Choose the field to edit (ID, Name, Course): ")
                    choice = choice.lower()

                    if choice == "id":
                        new_id = input("Enter new ID: ")
                        student.id = new_id
                        print("ID updated successfully.")
                    elif choice == "name":
                        new_name = input("Enter new name: ")
                        if not new_name:
                            print("Invalid input. Name cannot be blank.")
                            return
                        student.name = new_name
                        print("Name updated successfully.")
                    elif choice == "course":
                        new_course = input("Enter new course: ")
                        student.course = new_course
                        print("Course updated successfully.")
                    else:
                        print("Invalid choice.")
                        return

                    self.save_students()
                    return

            print("Student not found.")
        else:
            print("Student list is empty.")

    def edit_course(self):
            search = input("Enter search term (Code or Name): ")
            
            if self.courses:
                for course in self.courses:
                    if search in course.code or search in course.name:
                        print(f"Code: {course.code}, Name: {course.name}")

                        choice = input("Choose the field to edit (Code, Name): ")
                        choice = choice.lower()

                        if choice == "code":
                            new_id = input("Enter new code: ")
                            course.code = new_id
                            print("Code updated successfully.")
                        elif choice == "name":
                            new_name = input("Enter new name: ")
                            if not new_name:
                                print("Invalid input. Name cannot be blank.")
                                return
                            course.name = new_name
                            print("Name updated successfully.")
                        else:
                            print("Invalid choice.")
                            return

                        self.save_students()
                        return

                print("Student not found.")
            else:
                print("Student list is empty.")

    def search_student(self):
        search = input("Enter search term(Name or ID): ")
        if self.students:
            for student in self.students:
                if search in student.id or search in student.name:
                    print(f"Student found: ID: {student.id}, Name: {student.name}, Course: {student.course}")
                    return
                if not search in student.id and not search in student.name:
                    print("Student not found.")
                    return
        else:
            print("Student List is empty.")
   ############################################################################################################

    def list_students(self):
        if not self.students:
            print("No students found.")
        else:
            print("Id\tName\tCourses")
            for student in self.students:
                print(f"{student.id}\t{student.name}\t{student.course}\n")

    def list_courses(self):
        if not self.courses:
            print("No courses found.")
        else:
            print("Code\tName")
            for course in self.courses:
                print(f"{course.code}\t{course.name}")

############################################################################################################

ssis = SimpleStudentInformationSystem("studentinfo.txt","coursesinfo.txt")

ssis.run()
