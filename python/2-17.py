# タプルの利用
# タプルは要素の追加、変更、削除ができない　配列の定数みたいな感じ
scores = (70, 80, 55)
# scores[0] = 10  # 要素が変更できないため、実行するとエラーになる
"""error message
TypeError: 'tuple' object does not support item assignment
"""
print(scores)
print(scores[0])
print(f"要素数は{len(scores)}")
print(f"合計は{sum(scores)}")
