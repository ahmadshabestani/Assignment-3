num1 = int(input("Enter your Number :"))
num2 = int(input("Enter your Number : "))
number = 1

for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
        number = i

print(number)