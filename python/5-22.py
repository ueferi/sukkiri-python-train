def eat(breakfast, lunch, dinner="カレー"):
    """松田くんの食生活

    Args:
        breakfast (str): 朝食
        lunch (str): 昼食
        dinner (str, optional): 夕食. Defaults to "カレー".
    """
    print(f"朝は{breakfast}を食べました")
    print(f"昼は{lunch}を食べました")
    print(f"夜は{dinner}を食べました")


print("8月1日")
eat("トースト", "おにぎり")
print("8月2日")
eat("納豆ごはん", "ラーメン")
print("8月3日")
eat("バナナ", "そば", "焼肉")
print("8月4日")
eat("サンドイッチ", "しゅうまい弁当")
