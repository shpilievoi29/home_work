# Написать функцию перевода размеров женского белья из международного во все остальные.
# Внтри функции нужно просто обращаться к правильно составленному словарю.
xxs = {"RF": 42, "Germany": 36, "USA": 8, "France": 38, "GB": 24}
xs = {"RF": 44, "Germany": 38, "USA": 10, "France": 40, "GB": 26}
s = {"RF": 46, "Germany": 40, "USA": 12, "France": 42, "GB": 28}
m = {"RF": 48, "Germany": 42, "USA": 14, "France": 44, "GB": 30}
l = {"RF": 50, "Germany": 44, "USA": 16, "France": 46, "GB": 32}
xl = {"RF": 52, "Germany": 46, "USA": 18, "France": 48, "GB": 34}
xxl = {"RF": 54, "Germany": 48, "USA": 20, "France": 50, "GB": 36}
xxxl = {"RF": 56, "Germany": 50, "USA": 22, "France": 52, "GB": 38}

z = (input("Input international size:    "))
if z == str("xs"):
    print(xs)
elif  z == str("s"):
    print(xs)
elif z == str("xxs"):
    print(xxs)
elif z == str("l"):
    print(l)
elif z == str("xl"):
    print(xl)
elif z == str(xxl):
    print(xxl)
elif z == str("xxxl"):
    print(xxxl)
else:
    print(" Иди худей!")