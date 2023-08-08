# 年齢データから20代だけを一定数抽出するプログラム
# 不要な回のループをスキップする

ages = [28, 50, "ひみつ", 20, 78, 25, 22, 10, "無回答", 33]  # 対象データ
samples = list()  # サンプルデータを格納するリスト

for data in ages:
    if not isinstance(data, int):
        continue
    if data < 20 or data >= 30:
        continue
    samples.append(data)
print(samples)
