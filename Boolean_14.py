# Boolean14◦
#  Даны три целых числа: A, B, C. Проверить истинность высказывания: «Ровно одно из чисел A, B, C положительное».


a = int(input("Please enter A: "))
b = int(input("Please enter B: "))
c = int(input("Please enter C: "))


if a >= 0 and b < 0 and c < 0:
    print("True")
elif b >=0 and a < 0 and c < 0:
    print("True")
elif c >= 0 and a < 0 and b < 0:
    print("True")
else:
    print("False")      