# if文で答えが分岐するチャットボット
name = input("あなたの名前を教えてください>>")
print("{}さん、こんにちは".format(name))
food = input("{}さんの好きな食べ物を教えてください>>".format(name))
if "カレー" in food:  # 変数foodに"カレー"という文字列が含まれていれば、条件成立したことになる
    print("素敵です。カレーは最高ですよね！！")
else:
    print(f"私も{food}が好きですよ")
