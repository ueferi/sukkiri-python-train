# 1行日記を記録する
text = input("何を記録しますか>>")
with open("diary.txt", "a") as file:
    file.write(text + "\n")
