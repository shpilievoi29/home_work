number1=int(input("ВВедите число FIZZ" ))
number2=int(input("ВВедите число BUZZ" ))
number3=int(input("ВВедите чилсло, до которого проводить операции" ))
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



