grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = ['Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron']  # изменено на список

students_list = sorted(students)

# Вычисление средних оценок
grades_average_list = [sum(g) / len(g) for g in grades]  # использование list comprehension

# Создание словаря средних оценок
average_grades_dict = dict(zip(students_list, grades_average_list))
print(average_grades_dict)


