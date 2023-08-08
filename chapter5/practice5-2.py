def is_leapyear(y):
    """西暦を渡すとうるう年かどうかを判定する

    Args:
        y (int): 4桁の西暦年

    Returns:
        bool: 判定結果
    """
    return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)


current_year = int(input("現在の西暦を入力してください>>"))
if is_leapyear(current_year):
    print(f"西暦{current_year}は、うるう年です")
else:
    print(f"西暦{current_year}は、うるう年ではありません")
