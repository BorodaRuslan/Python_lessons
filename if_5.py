# If5. Даны три целых числа. Найти количество положительных и количество отрицательных чисел в исходном набор

a = int(input("Please enter A: "))
b = int(input("Please enter B: "))
c = int(input("Please enter C: "))


positive_number = 0;
negative_number = 0;

if a >= 0:
    positive_number = positive_number + 1
else:
    negative_number = negative_number + 1

if b >= 0:
    positive_number = positive_number + 1
else:
    negative_number = negative_number + 1


if c >= 0:
    positive_number = positive_number + 1
else:
    negative_number = negative_number + 1


print(f"Positive number count: {positive_number} ")  
print(f"Negative number count: {negative_number} ")  
