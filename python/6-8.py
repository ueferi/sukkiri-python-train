# 防御的コピー
def add_suffix(names):
    """渡されたリスト内の名前に「さん」を付ける関数

    Args:
        names (str): 名前

    Returns:
        str: 名前に「さん」が付いている状態
    """
    for i in range(len(names)):
        names[i] += "さん"
    return names


before_names = ["松田", "浅木", "工藤"]
copied_names = list()  # リストを複製する
for n in before_names:
    copied_names.append(n)

after_names = add_suffix(before_names)  # 複製したリストを関数に渡す

print(f"さん付け後:{after_names[0]}")  # add_suffixから返されたリスト内の先頭の要素
print(f"さん付け前:{before_names[0]}")
