char_user = input("Enter your char :")
counter = 0
n = []
for i in range(len(char_user)):
    if char_user[i] != " ":
        n.append(char_user[i])
    else:
        counter += 1

print(counter+1)