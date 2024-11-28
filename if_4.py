
# Даны три целых числа. Найти количество положительных чисел в наборе.



a = int(input("Please enter A: "))
b = int(input("Please enter B: "))
c = int(input("Please enter C: "))


count = 0

if a >= 0:
    count = count + 1
if b >= 0:
    count = count + 1    
if c >= 0:
    count = count + 1

print(f"Positive number count: {count}")        