number = int(input("Введите целое число: "))
print("Делители данного числа:", end=" ")
for x in range(number, 1, -1):
    if (number % x == 0):
        print(x, end="   ")
print("Разряды данного числа:", end=" ")
while number > 0:
    print(number % 10, end=",")
    number=number // 10
