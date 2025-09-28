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
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

print(student.marks(lecturer, 'Python', 7))  # None
print(student.marks(lecturer, 'Java', 8))  # Ошибка
print(student.marks(lecturer, 'С++', 8))  # Ошибка
print(student.marks(reviewer, 'Python', 6))  # Ошибка

print(lecturer.grades)  # {'Python': [7]}
print(lecturer)
print(reviewer)
print(student)