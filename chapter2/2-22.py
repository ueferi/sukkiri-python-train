# セットの利用

"""セットの特徴
- 重複する値は格納できない
- 添え字やキーが存在しない
- セットの要素には順序がない
- セットに値を追加するときはadd関数を使う
"""

scores = {70, 80, 55, 80}  # 80がダブっている
scores.add(80)  # さらに80を追加
print(scores)
print(f"要素数は{len(scores)}")
print(f"合計は{sum(scores)}")
