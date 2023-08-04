# 繰り返しによるリスト要素の利用
scores = [80, 20, 75, 60]
count = 0
while count < len(scores):
    if scores[count] >= 60:
        print("合格")
    else:
        print("不合格")
    count += 1

# 上記をfor文に書き換えてみる
scores = [80, 20, 75, 60]
for data in scores:
    if data >= 60:
        print("合格")
    else:
        print("不合格")
