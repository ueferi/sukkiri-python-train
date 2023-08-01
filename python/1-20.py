# 割り勘計算プログラム
price = input("料金を入力>>")  # キーボード入力結果はstr型
price = int(price)
number = input("人数を入力>>")  # キーボード入力結果はstr型
number = int(number)
payment = price / number  # 割り算の結果はfloat型
payment = int(payment)
print("お支払いは" + str(payment) + "円です")  # 文字列と数値を連結できないのでstr型変換している

# f-stringを使ってもっと簡素に書く
price = input("料金を入力>>")  # キーボード入力結果はstr型
price = int(price)
number = input("人数を入力>>")  # キーボード入力結果はstr型
number = int(number)
payment = price / number  # 割り算の結果はfloat型
payment = int(payment)
print(f"お支払いは{payment}円です")  # !こっちの方が上の書き方より直観的で分かりやすい
