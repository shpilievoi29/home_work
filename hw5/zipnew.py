# Содать свой ZIP



a = [5, 6, 7, 8, 1, 12]
b = [1, 2, 3, 4, 5, 6]

for pair in ((a[i], b[i]) for i in range(min(len(a), len(b)))):
    print(pair)