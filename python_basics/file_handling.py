# import random

# def game():
#     score = random.randint(1,61)
#     print(f"Your score is : {score}")
#     with open("file.txt") as f:
#         highscore = f.read()
#         if(highscore != ""):
#             highscore = int(highscore)
#         else: highscore = 0

#     if(highscore < score):
#         print("score added")
#         with open("file.txt", "w") as f:
#             f.write(str(score))
        
# game()



# with open("file.txt") as f:
#     content = f.read()
# newContent = content.replace("Hey", "Chal")

# with open("file.txt" ,"w") as f:
#     f.write(newContent)


words = ["Chal", "nikal"]
with open("file.txt") as f:
    content = f.read()
for word in words:
    content = content.replace(word, "*" * len(word))

with open("file.txt" ,"w") as f:
    f.write(content)