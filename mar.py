n = int(input("Enter your Number :"))
array = []
for i in range(0, n):
    array.append("*#")

for i1 in range(0, len(array)):
    print(array[i1], end=" ")
