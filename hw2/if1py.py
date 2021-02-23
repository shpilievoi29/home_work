radius = int(input("Введите радиус: "))

if radius >= 0:
    print("Длина окружности = ",  2  *  3.14  *  radius)
    print("Площадь = ", 3.14 * radius ** 2)
else:
    print("Пожалуйста, введите положительное число")