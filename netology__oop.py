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
        sum_student_marks = 0
        i = 0
        for v in self.grades.values():
            sum_student_marks += v
            i += 1

        srznach = sum_student_marks / i
        return srznach

    def __str__(self):
        return f"""Имя:{self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self.val(self.grades)}
Курсы в процессе изучения: {",".join(self.courses_in_progress)}
Завершенные курсы: Введение в программирование {",".join(self.finished_courses)}"""

    def __gt__(self, other):
        return self.val(self.grades) > other.val(other.grades)

    def __le__(self, other):
        return self.val(self.grades) <= other.val(other.grades)

    def __eq__(self, other):
        return self.val(self.grades) == other.val(other.grades)


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
        sum_lestur_marks = 0
        i = 0
        for v in self.grades.values():
            sum_lestur_marks += v
            i += 1
        srznach = sum_lestur_marks / i
        return srznach

    def __str__(self):
        return f"""Имя:{self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self.value(self.grades)}
"""

    def __gt__(self, other):
        return self.value(self.grades) > other.value(other.grades)

    def __le__(self, other):
        return self.value(self.grades) <= other.value(other.grades)

    def __eq__(self, other):
        return self.value(self.grades) == other.value(other.grades)

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def __str__(self):
        return f"""Имя: {self.name}
Фамилия: {self.surname}"""


def compare_students(list_st, course):
    sum_st = 0
    count_st = 0
    for i in list_st:
        if isinstance(i, Student):
            for key in i.grades.keys():
                if key == course:
                    value = i.grades[course]
                    sum_st += value
                    count_st += 1
    sredn_st = sum_st/count_st
    return sredn_st


def compare_lecturers(list_l, course):
    sum_l = 0
    count_l = 0
    for i in list_l:
        if isinstance(i, Lecturer):
            for key_l in i.grades.keys():
                if key_l == course:
                    value_l = i.grades[course]
                    sum_l += value_l
                    count_l += 1
    sredn_l = sum_l/count_l
    return sredn_l








#Тестирование
student_1=Student("Олег", "Молчанов", "М")
student_2=Student("Мария", "Спирина", "Ж")
student_3=Student("Александр", "Ушаков", "М")

student_1.courses_in_progress += ['Python', 'Java']
student_2.courses_in_progress += ['Python', 'Java', 'C++']
student_3.courses_in_progress += ['Python', 'C++']

reviewer_1=Reviewer("Дарья", "Андреева")
reviewer_1.courses_attached += ['Python', 'C++']
reviewer_2=Reviewer("Михаил", "Анисимов")
reviewer_2.courses_attached += ['Python', 'C']

lecturer_1 = Lecturer("Дмитрий", "Васильев")
lecturer_2 = Lecturer("Анна", "Барсукова")
lecturer_3 = Lecturer("Ксения", "Буланова")
lecturer_1.courses_attached += ['Java','Python','C']
lecturer_2.courses_attached += ['Java','Python','C++']
lecturer_3.courses_attached += ['Java','Python','SQL']

student_1.marks(lecturer_3, "Python", 5)
student_1.marks(lecturer_2, "Python", 8)
student_2.marks(lecturer_1, "Java", 4)
student_1.marks(lecturer_2, "Java", 10)
student_3.marks(lecturer_2, "C++", 7)

student_1.marks(reviewer_1, "Python", 9)
student_2.marks(reviewer_1, "Python", 10)
student_3.marks(reviewer_2, "Python", 6)

print(student_1.__str__())
print(student_2.__le__(student_3))
print(student_1.__eq__(student_2))
print(student_3.__gt__(student_1))
print(lecturer_2.__eq__(lecturer_3))
print(student_3.__gt__(student_2))
print(student_2.__le__(student_1))
print(lecturer_1.__str__())
print(reviewer_2.__str__())
compare_list_l = [lecturer_1, lecturer_2, lecturer_3]
compare_list_st = [student_1, student_2, student_3]
print(compare_students(compare_list_st, "Python"))
print(compare_lecturers(compare_list_l, 'Java'))










# lecturer = Lecturer('Иван', 'Иванов')
# reviewer = Reviewer('Пётр', 'Петров')
# print(isinstance(lecturer, Mentor)) # True
# print(isinstance(reviewer, Mentor)) # True
# print(lecturer.courses_attached)    # []
# print(reviewer.courses_attached)    # []
#
# lecturer = Lecturer('Иван', 'Иванов')
# lecturer_2 = Lecturer('Андрей', 'Козлов')
# lecturer_2.courses_attached += ['Python', 'C++']
#
# reviewer = Reviewer('Пётр', 'Петров')
# student = Student('Алёхина', 'Ольга', 'Ж')
# student_2 = Student('Алёхин', 'Лев', 'М')
#
#
# student.courses_in_progress += ['Python', 'Java']
# student_2.courses_in_progress += ['Python', 'Java', 'C++']
#
# lecturer.courses_attached += ['Python', 'C++']
# reviewer.courses_attached += ['Python', 'C++']
#
# print(student.marks(lecturer, 'Python', 7))  # None
# print(student.marks(lecturer, 'Java', 8))  # Ошибка
# print(student.marks(lecturer, 'С++', 8))  # Ошибка
# print(student.marks(reviewer, 'Python', 6))  # Ошибка
# print(student_2.marks(reviewer, 'C++', 9))  # Ошибка
#
# print(student.marks(lecturer_2, 'Python', 5))  # None
#
# print(lecturer.grades)  # {'Python': [7]}
# print(lecturer)
# print(reviewer)
# print(student)
# print(lecturer.__cmp__(lecturer_2))
# print(student.__cmp__(student_2))