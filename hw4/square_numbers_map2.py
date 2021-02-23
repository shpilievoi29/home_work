# Написать функцию которая будет простое число возводить в квардрат.

# Необходимо возвести в квадрат все простые числа в списке используя функцию map


def square_number(nums):
    for z in range(2, nums):
        if nums % z:
            continue
        else:
            return nums
    return nums **2


numbers = [1, 2, 3, 4,  5, 6, 7, 9, 11, 12, 13, 14, 17, 19, 23, 29]


new_numbers = list(map(square_number, numbers))

print(new_numbers)
