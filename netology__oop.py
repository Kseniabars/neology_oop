class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def marks(self, mentor, course, grade):
        if ((isinstance(mentor, Lecturer) or isinstance(mentor, Reviewer)) and (course in self.courses_in_progress)
                and (course in mentor.courses_attached)):
            if isinstance(mentor, Lecturer):
                if course in mentor.grades:
                    mentor.grades[course] += grade
                else:
                    mentor.grades[course] = grade
            elif isinstance(mentor, Reviewer):

                if course in self.grades:
                    self.grades[course] += grade
                else:
                    self.grades[course] = grade
        else:
            return "Ошибка"

    def val(self, grades):
        sum = 0
        i = 0
        for v in self.grades.values():
            sum += v
            i += 1

        srznach = sum // i
        return srznach

    def __str__(self):
        return f"""Имя:{self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self.val(self.grades)}
Курсы в процессе изучения: {",".join(self.courses_in_progress)}
Завершенные курсы: Введение в программирование {",".join(self.finished_courses)}"""

    def __cmp__(self, other):
        if self.val(self.grades)< other.val(other.grades):
            return -1
        elif self.val(self.grades)> other.val(other.grades):
            return 1
        else:
            return 0
class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}
    def value(self, grades):
        sum=0
        i=0
        for v in self.grades.values():
            sum+=v
            i+=1
        srznach = sum // i
        return srznach

    def __str__(self):
        return f"""Имя:{self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self.value(self.grades)}
"""
    def __cmp__(self, other):
        if self.value(self.grades)< other.value(other.grades):
            return -1
        elif self.value(self.grades)> other.value(other.grades):
            return 1
        else:
            return 0

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def __str__(self):
        return f"""Имя: {self.name}
Фамилия: {self.surname}"""





lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
print(isinstance(lecturer, Mentor)) # True
print(isinstance(reviewer, Mentor)) # True
print(lecturer.courses_attached)    # []
print(reviewer.courses_attached)    # []

lecturer = Lecturer('Иван', 'Иванов')
lecturer_2 = Lecturer('Андрей', 'Козлов')
lecturer_2.courses_attached += ['Python', 'C++']

reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')
student_2 = Student('Алёхин', 'Лев', 'М')


student.courses_in_progress += ['Python', 'Java']
student_2.courses_in_progress += ['Python', 'Java', 'C++']

lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

print(student.marks(lecturer, 'Python', 7))  # None
print(student.marks(lecturer, 'Java', 8))  # Ошибка
print(student.marks(lecturer, 'С++', 8))  # Ошибка
print(student.marks(reviewer, 'Python', 6))  # Ошибка
print(student_2.marks(reviewer, 'C++', 9))  # Ошибка

print(student.marks(lecturer_2, 'Python', 5))  # None

print(lecturer.grades)  # {'Python': [7]}
print(lecturer)
print(reviewer)
print(student)
print(lecturer.__cmp__(lecturer_2))
print(student.__cmp__(student_2))