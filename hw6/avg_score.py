# Создать словарь оценок предполагаемых студентов (Ключ - ФИ студента, значение - список оценок студентов).
# Найти самого успешного и самого отстающего по среднему баллу.


students = {'Иванов Иван': [6, 5, 9], 'Петров Петр': [5, 8, 10], 'Андреев Андрей': [9, 8, 10],
            'Борисов Борис': [6, 5, 3], 'Григорий Малков': [5, 6, 10]}
name_values = (students.keys())

dict_valuse = (students.values())


def sum_values(num):
    return float(sum(num)) / (len(num))


average_list = list(map(sum_values, dict_valuse))
final_list = dict(zip(name_values, average_list))
print(final_list)

