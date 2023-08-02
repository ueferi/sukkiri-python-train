# 2-2 5教科の試験結果を入力し、合計点と平均点を表示する
scores = list()
scores.append(int(input("国語の試験結果を入力>>")))
scores.append(int(input("算数の試験結果を入力>>")))
scores.append(int(input("理科の試験結果を入力>>")))
scores.append(int(input("社会の試験結果を入力>>")))
scores.append(int(input("英語の試験結果を入力>>")))
avg = sum(scores) / len(scores)  # 平均は合計をlen(scores)で割る
print(f"合計点は{sum(scores)}、平均点は{avg}")

# 2-3 相性診断プログラム
player1 = {"料理", "フラワーアレンジメント", "薬草茶"}
player2 = {"旅行", "料理"}
input("心の準備ができたらEnterキーを押してね")
result = len(player1 & player2) / len(player1 | player2) * 100
print(f"相性は{result}%")
