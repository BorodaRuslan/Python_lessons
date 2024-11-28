#Арифметические действия над числами пронумерованы следующим
#образом: 1 — сложение, 2 — вычитание, 3 — умножение, 4 — деление. Дан
#номер действия N (целое число в диапазоне 1–4) и вещественные числа A
#и B (В не равно 0). Выполнить над числами указанное действие и вывести
#результат.


number_one = float(input("Please enter first number: "))
number_two = float(input("Please enter second number: "))

action = int(input("Please Select an action (1-4) : "))
result = None

if action == 1:
    result = number_one + number_two
elif action == 2:
     result = number_one - number_two
elif action == 3:
     result = number_one * number_two
elif action == 4:
     result = number_one / number_two
else:
     print("Invalid input!")                  

print(f"Result: {result}")