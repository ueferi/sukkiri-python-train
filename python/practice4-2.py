count = 1
answer = True
print("カレーを召し上がれ")
while answer == True:
    print(f"{count}皿のカレーを食べました")
    key = input("おかわりはいかがですか (y/n)>>")
    if key == "y":
        count += 1
    else:
        answer = False
print("ごちそうさまでした")
