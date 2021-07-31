def if_statement():
    # 変数の評価
    x1 = 0
    if x1:
        print('{} is Truthy'.format(x1))
    else:
        print('{} is Falsy'.format(x1)) # こちらを通る

    x2 = 1
    if x2:
        print('{} is Truthy'.format(x2)) # こちらを通る
    else:
        print('{} is Falsy'.format(x2))

    x3 = []
    if x3:
        print('{} is Truthy'.format(x3))
    else:
        print('{} is Falsy'.format(x3)) # こちらを通る

    x4 = [0]
    if x4:
        print('{} is Truthy'.format(x4)) # こちらを通る
    else:
        print('{} is Falsy'.format(x4))

    x5 = {}
    if x5:
        print('{} is Truthy'.format(x5))
    else:
        print('{} is Falsy'.format(x5)) # こちらを通る

    x6 = {"key": 0}
    if x4:
        print('{} is Truthy'.format(x6)) # こちらを通る
    else:
        print('{} is Falsy'.format(x6))

    # elif/elseブロック
    x = 23
    if x % 2 == 0:
        print("xは2の倍数です。")
    elif x % 3 == 0:
        print("xは3の倍数です。")
    else:
        print("xは2の倍数でも3の倍数でもありません。")

    # 三項演算子
    age = 10
    str = "majority" if age >= 20 else "minority"
    print(str)

    age = 40
    str = "majority" if age >= 20 else "minority"
    print(str)

if_statement()

def for_statement():
    # 指定回数ループ
    for i in range(3):
        print("Hello")
    
    # ループカウンタを使う
    l = ['a', 'b', 'c']
    for idx, val in enumerate(l):
        if idx != 0:
            print(idx, val)

    # zip関数
    list1 = ["a", "b", "c"]
    list2 = [1, 2, 3]
    for x, y in zip(list1, list2):
        print(x, y)

    # 逆順にループ処理(reversed使用)
    l = [1, 2, 3, 4, 5]
    for x in reversed(l):
        print(x)

    # 逆順にループ処理(スライス構文使用)
    for x in l[::-1]:
        print(x)
    
    # リスト内包表記
    list1 = [1, 2, 3]
    list2 = [val * 2 for val in list1]
    print(list2)

    # リスト内包表記(条件分岐あり)
    list2 = [val * 2 for val in list1 if val % 2 == 1]
    print(list2)

    # 集合内包表記
    set1 = {val * 2 for val in list1}
    print(set1)

    # リスト内包表記(条件分岐あり)
    set2 = {val * 2 for val in list1 if val % 2 == 1}
    print(set2)

    # 辞書内包表記
    dict1 = {val: 0 for val in list1}
    print(dict1)

    # 辞書内包表記(条件分岐あり)
    dict2 = {val: 0 for val in list1 if val >= 2}
    print(dict2)

for_statement()