# f12 Даны три числа. Найти наименьшее из них


a = 5
b = 6
c = 7


if a < b and a < c:
    print(f"Min is a: {a}")

if b < a and b < c:
    print(f"Min is b: {b}")

if c < a and c < b:
    print(f"Min is c: {c}")    

if a == b and a == c:
    print("all numbers are equal")
