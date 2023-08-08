# randomモジュールのrandint関数をインポート
from random import randint

print("数当てゲームを始めます。3桁の数を当ててください！")

# 答えを格納する空のanswerリストを作成
answer = list()
# 0~9までのランダムな整数を3つ格納する
for n in range(3):
    answer.append(randint(0, 9))  # answerリストに追加

# 予想の入力
should_continue = True  # *動詞の挙動を行うべきか尋ねる　ので、should+動詞原型
while should_continue == True:
    # 入力された整数を格納する空のpredictionリストを作成
    prediction = list()
    for n in range(3):
        data = int(input(f"{n+1}桁目の予想を入力(0~9)>>"))
        prediction.append(data)  # predictionリストに追加

    # answerリストとpredictionリストを比較
    hit = 0  # 位置と数値が位置する要素
    ball = 0  # 位置は異なるが数値が一致する要素

    for n in range(3):  # 3回入力受付しながら判定する
        if prediction[n] == answer[n]:  # hit加算
            hit += 1
        else:
            for m in range(3):
                if prediction[n] == answer[m]:  # ball加算
                    ball += 1
                    break

    # 結果を表示
    print(f"{hit}ヒット！{ball}ボール！")
    if hit == 3:  # 3桁とも正解の場合
        print("正解です！")
        should_continue = False  # 正解のためゲームを終了
    else:  # 不正解の場合
        if int(input("続けますか? 1:続ける 2:終了 >>")) == 2:
            print(f"正解は{answer[0]}{answer[1]}{answer[2]}")
            should_continue = False  # 2:終了が入力されたためゲームを終了
