# 関数の定義と呼び出し
def hello(name):
    print(f"こんにちは。{name}です。")


hello("浅木")
hello("松田")


def profile(name, age, hobby):
    """複数の引数を受け取るprofile関数

    Args:
        name (str): 名前
        age (int): 年齢
        hobby (str): 趣味
    """
    print(f"私の名前は{name}です。")
    print(f"年齢は{age}歳です。")
    print(f"趣味は{hobby}です。")


profile("浅木", 24, "カフェ巡り")
