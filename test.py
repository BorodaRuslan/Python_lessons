
# 5, 9, 10

a = int(input("Please enter number: "))
b = int(input("Please enter number: "))
c = int(input("Please enter number: "))


min_number = a

if b < min_number:
    min_number = b
if c < min_number:
    min_number = c

print(f"Минимальное число: {min_number}")        
