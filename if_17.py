# If17. Даны три переменные вещественного типа: A, B, C. Если их значения
# упорядочены по возрастанию или убыванию, то удвоить их; в противном случае заменить значение каждой переменной на противоположное.
# Вывести новые значения переменных A, B, C


a = float(input("Please enter A: "))
b = float(input("Please enter B: "))
c = float(input("Please enter C: "))


if (a > b > c) or (a < b < c):
    a = a * 2
    b = b * 2 
    c = c * 2
else:
    a = -a
    b = -b
    c = -c 

print(f"a: {a} b: {b} c: {c}")    
