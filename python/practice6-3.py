# 6-3
def welcome(u):
    print(f"ようこそ{u['name']}さん")
    u["age"] += 1
    print(f"あなたは来年{u['age']}歳だから大吉です！")


username = input("名前を入力してください>>")
userage = int(input("年齢を入力してください>>"))
user = {"name": username, "age": userage}
copied_user = user.copy()  # 防御的コピー
welcome(copied_user)
print(f"{user['age']}歳の{user['name']}さん、またプレイしてくださいね")
