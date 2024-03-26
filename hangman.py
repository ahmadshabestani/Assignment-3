import random

words_bank = ["tree", "book", "blue", "fish", "life", "iran", "sky", "freedom", "train"]
# words_counter = random.randint(0, len(words_bank) - 1)
# print(words_bank[words_counter])
words = random.choice(words_bank)
user_mistakes = 0
good_chars = []
bad_chars = []
while user_mistakes < 6:
    for i in range(len(words)):
        if words[i] in good_chars:
            print(words[i], end=" ")
        else:
            print(" - ", end=" ")
    user_char = input("please write your guess : ")
    if len(user_char) == 1:
        # print(words)
        if user_char.lower() in words:
            good_chars.append(user_char.lower())
            if len(good_chars) == len(words):
                print("you win")
                print(words)
                break
        else:
            bad_chars.append(user_char.lower())
            user_mistakes += 1
    else:
        print("Enter one char")
        user_mistakes += 1
if user_mistakes == 6:
    print("Game Over!")