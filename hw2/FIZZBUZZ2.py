number1 = int(2)
number2 = int(5)
number3 = int(18)
i=int(0)
while i <= number3-1:
    i += 1
    if i % number1 == 0 and i % number2 == 0:
        print("FB", end="")
    elif i % number1 == 0:
        print ("F", end="")
    elif i % number2 ==0:
        print("B", end="")
    else:
        print(i, end="")



