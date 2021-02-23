number = int(input("Введите целое число: "))
print("Делители данного числа:", end = " ")
for x in range(number, 1, -1):
    if (number % x == 0):
        print(x, end = ",")

