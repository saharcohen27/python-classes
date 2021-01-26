class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_person(self):
        print(f"My name is {self.name} and I'm {self.age} years old")

    def print_birthyear(self):
        print(2020 - self.age)


class Student(Person):
    def __init__(self, name, age, id_number):
        super().__init__(name, age)
        self.id_number = id_number
        self.grades = []

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def add_grade(self, grade):
        self.grades.append(grade)

    def remove_grade(self, grade):
        try:
            self.grades.remove(grade)
        except ValueError:
            print(f"[ERROR!] {grade} not in list")

    def learn(self):
        print("I'm learning")

    def __eq__(self, student2):
        try:
            return self.id_number == student2.id_number
        except AttributeError:
            print(f"[ERROR!] Not a Student")
            return False


class GiftedStudent(Student):
    def __init__(self, name, age, id_number, iq):
        super().__init__(name, age, id_number)
        self.iq = iq

    def learn(self):
        print("I'm learning a lot")

    def __eq__(self, gifted_student2):
        try:
            return self.id_number == gifted_student2.id_number
        except AttributeError:
            print(f"[ERROR!] Not a Student")
            return False

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_id(self, id2):
        self.id_number = id2

    def set_iq(self, iq):
        self.iq = iq

    def get_id(self):
        return self.id_number

    def get_iq(self):
        return self.iq

    def get_grades(self):
        return self.grades


class MyClass():
    def __init__(self, class_name, class_number):
        self.students = []
        self.class_name = class_name
        self.class_number = class_number

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
        else:
            print("[ERROR!] User not found")

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
        else:
            print("[ERROR!] User already in class")

    def start_learn(self):
        for student in self.students:
            student.learn()

    def print_all_students(self):
        names = []
        for student in self.students:
            names.append(student.get_name())

        print(f"{self.class_name} | {self.class_number} \n {', '.join(names)} \n")


class MyGiftedClass(MyClass):
    def __init__(self, class_name, class_number):
        super().__init__(class_name, class_number)

    def set_class_name(self, name):
        self.class_name = name

    def set_class_number(self, number):
        self.class_number = number

    def get_class_name(self):
        return self.class_name

    def get_class_number(self):
        return self.class_number

    def add_student(self, gifted_student):
        try:
            gifted_student.get_iq()
        except AttributeError:
            print("[ERROR!] Not a Gifted Student")
            return

        if gifted_student not in self.students:
            self.students.append(gifted_student)
        else:
            print("[ERROR!] User already in class")


class MySchool():
    def __init__(self):
        self.classes = []

    def add_class(self, class1):
        if isinstance(class1, MyClass) or isinstance(class1, MyGiftedClass):
            if class1 not in self.classes:
                self.classes.append(class1)
            else:
                print("[ERROR!] Already exists")
        else:
            print("[ERROR!] Not a class")

    def remove_class(self, class1):
        if isinstance(class1, MyClass) or isinstance(class1, MyGiftedClass):
            if class1 in self.classes:
                self.classes.remove(class1)
            else:
                print("[ERROR!] Class not in school")
        else:
            print("[ERROR!] Not a class")

    def print_all_students_names(self):
        for cls in self.classes:
            cls.print_all_students()


if __name__ == '__main__':
    # creating 2 regular students
    student1 = Student("shrem", 17, 123789456)
    student2 = Student("musli", 18, 987231654)

    # creating 2 gifted students
    gifted_student1 = GiftedStudent("sahar", 17, 123456789, 200)
    gifted_student2 = GiftedStudent("rotem", 16, 987654321, 200)

    # creating regular class
    regular_class = MyClass("Normal Class", 1)
    # creating gifted class
    gifted_class = MyGiftedClass("Gifted Class", 2)

    # adding all 4 students to the regular class
    regular_class.add_student(student1)
    regular_class.add_student(student2)
    regular_class.add_student(gifted_student1)
    regular_class.add_student(gifted_student2)

    # adding all 4 students to the gifted class
    gifted_class.add_student(student1)
    gifted_class.add_student(student2)
    gifted_class.add_student(gifted_student1)
    gifted_class.add_student(gifted_student2)

    # start learn for both classes
    regular_class.start_learn()
    gifted_class.start_learn()

    # createing school
    school = MySchool()
    # adding the classes to the school
    school.add_class(regular_class)
    school.add_class(gifted_class)
    # printing all students names * also kind of sorting by classes
    school.print_all_students_names()
