#If18. Даны три целых числа, одно из которых отлично от двух других, равных между собой. 
# Определить порядковый номер числа, отличного отостальных

a = int(input("Please enter A: "))
b = int(input("Please enter B: "))
c = int(input("Please enter C: "))



if a == b:
    result = 3
elif a == c:
    result = 2
else:
    result = 1   

print(result)





