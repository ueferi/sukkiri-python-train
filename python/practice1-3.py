# BMIを求めるプログラム
# BMIの計算式：BMI = weight(kg) / height(m) / height(m)
height = int(input("Put your height(cm) here>>"))
weight = int(input("Put your weight(kg) here>>"))
height_m = height / 100  # cmをmに変換するために100で割る
bmi = weight / height_m / height_m
print(f"Your BMI is {bmi}")
