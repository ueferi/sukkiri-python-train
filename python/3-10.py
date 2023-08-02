# 晩ごはんをレコメンドするチャットボット
print("Answer all questions with y or n")
okane_aruka = input("Do you have enough money?>>")

if okane_aruka == "y":
    onaka_suiteruka = input("Do you feel very hungry?>>")
    nomitai_kibunka = input("Do you want to drink beer?>>")
    if onaka_suiteruka == "y" and nomitai_kibunka == "y":
        print("How about Yakiniku?")
    elif onaka_suiteruka == "y":
        print("How about curry?")
    elif nomitai_kibunka == "y":
        print("How about Yakitori?")
    else:
        print("How about pasta?")
    yashoku_iruka = input("Do you need a nightly meal?>>")
    if yashoku_iruka == "y":
        print("How about chicken from convenient stores?")
else:
    print("Don't eat out")
