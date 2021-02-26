# Банкомат выдает сумм мелкими, но не больше 10 штук каждой мелкой купюры

z = sum = int(input("Input sum multiple of 10:      "))

thousand = 0
five_hundred = 0
two_hundred = 0
one_hundred = 0
fifty = 0
twenty = 0
ten = 0

while z > 0:
    if z >= 8800:
        thousand = ((z - 8800) // 1000) + 1
        z = z - (thousand * 1000)
    elif (z < 8800) and (z >= 3800):
        five_hundred = (((z - 3800)) // 500) + 1
        z = z - five_hundred * 500
    elif (z < 3800) and (z >= 1800):
        two_hundred = (((z - 1800)) // 200) + 1
        z = z - two_hundred * 200
    elif (z < 1800) and (z >= 800):
        one_hundred = (((z - 800)) // 100) + 1
        z = z - one_hundred * 100
    elif (z < 800) and (z >= 300):
        fifty = (((z - 300)) // 50) + 1
        z = z - fifty * 50
    elif (z < 300) and (z >= 100):
        twenty = (((z - 100)) // 20) + 1
        z = z - twenty * 20
    elif z < 100:
        ten = z // 10
        z = z % 10
print('nominal 1000: ' + str(thousand))
print('nominal 500: ' + str(five_hundred))
print('nominal 200: ' + str(two_hundred))
print('nominal 100: ' + str(one_hundred))
print('nominal 50: ' + str(fifty))
print('nominal 20: ' + str(twenty))
print('nominal 10: ' + str(ten))
