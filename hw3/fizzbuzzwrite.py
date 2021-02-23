#Переделать FIZZBUZZ так, чтобы результат писался в другой файл.


f = open("fizz.txt", "r")
z = open("write.txt", "w")

for i in f:

    line = list(map(int, i.split()))
    line1 = int(line[0])
    line2 = int(line[1])
    line3 = int(line[2])

    s = int()
    for s in range(1, line3 +1):
        if s % line1 == 0 and s % line2 == 0:
            z.write("FB" + ',')
        elif s % line2 == 0:
            z.write("F"+ ',')
        elif s % line1 == 0:
            z.write("B"+ ',')
        else:
            z.write(str(s) + ',')
    z.write('\n')
f.close()
z.close()
