# 関数さえオブジェクトとして扱う
def add(x, y):
    return x + y


print(type(add))  # <class 'function'>
newadd = add
print(newadd(4, 5))
