tedad_arraye = int(input("tedad araye ra vared konid :"))
array = []
for i in range(0,tedad_arraye):
    user_number = int(input("Enter your Number :"))
    if user_number in array:
        continue
    array.append(user_number)
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
print(array)



