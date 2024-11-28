
# Boolean12◦
# Даны три целых числа: A, B, C. Проверить истинность высказывания: «Каждое из чисел A, B, C положительное».


a = int(input("Please enter A: "))
b = int(input("Please enter B: "))
c = int(input("Please enter C: "))


if a >= 0 and b >= 0 and c >= 0:
    print("True")
else:
    print("False")    