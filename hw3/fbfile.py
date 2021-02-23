# Написать fizzbuzz для 20 троек чисел, которые записаны в файл. Читаете из файла первую строку,
# берете из нее числа, считаете для них fizzbuzz, выводите.


f = open("fizz.txt", "r")

for i in f:

    line = list(map(int, i.split()))
    line1 = int(line[0])
    line2 = int(line[1])
    line3 = int(line[2])

    s = int()
    for s in range(1, line3 +1):
        if s % line1 == 0 and s % line2 == 0:
            print("FB", end=",")
        elif s % line2 == 0:
            print("F", end=",")
        elif s % line1 == 0:
            print("B", end=",")
        else:
            print(s, end=",")
    print("")
f.close()
