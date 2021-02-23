# Создать структуру данных для студентов из имен и фамилий, можно случайных.
# Придумать структуру данных, чтобы указывать, в какой группе
# учится студент (Группы Python, FrontEnd, FullStack, Java). Студент может учиться в нескольких группах.
# Затем вывести:
# студентов, которые учатся в двух и более группах
# студентов, которые не учатся на фронтенде
# студентов, которые изучают Python или Java
students = {'Иванов Иван', 'Петров Петр', 'Андреев Андрей', 'Борисов Борис', 'Григорий Малков', 'Александр Шпилевой'}

java_students = {'Иванов Иван', 'Петров Петр', 'Андреев Андрей'}

python_students = {'Александр Шпилевой', 'Борисов Борис' }

frontend_students = {'Борисов Борис', 'Андреев Андрей'}

fullstack_students = {'Григорий Малков', 'Иванов Иван', 'Борисов Борис'}

print("Студенты, которые не учатся на FrontEnd:     ", students - frontend_students)
print("Студенты Python или Java:   ", python_students | java_students)
print("Студенты, которые учатся в двух и более группах:   ",java_students & python_students,
      java_students & frontend_students, java_students & fullstack_students, python_students & frontend_students,
      python_students & fullstack_students, frontend_students & fullstack_students)


