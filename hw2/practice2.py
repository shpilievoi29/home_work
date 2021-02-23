number=int(input("ВВедите целое число" ))
if number % 2==1 and number % 3==0 and number % 5==0 and number % 10==5 :
    print("Это число, которое мы искали")
else:
    print("Это число нам не подходит")
