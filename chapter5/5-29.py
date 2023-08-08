def eat(breakfast, lunch, dinner="カレー", *desserts):
    """おやつも出力できるeat関数

    Args:
        breakfast (str): 朝食
        lunch (str): 夕食
        dinner (str, optional): 夕食. Defaults to "カレー".
    """
    print(f"朝は{breakfast}を食べました")
    print(f"昼は{lunch}を食べました")
    print(f"晩は{dinner}を食べました")
    for d in desserts:
        print(f"おやつに{d}を食べました")


eat("トースト", "パスタ", "カレー", "アイス", "チョコ", "カレー")
