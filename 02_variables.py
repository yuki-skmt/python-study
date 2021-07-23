'''
変数
'''

from keyword import kwlist

# 予約語一覧
def show_keyword():
    print(kwlist)

# 基本の組み込みデータ型
# int
def int_type():
    x = 100
    y = 3

    # 加算
    print(x + y)

    # 減算
    print(x - y)

    # 乗算
    print(x * y)

    # 除算
    print(x / y)

    # 商
    print(x // y)

    # 剰余
    print(x % y)

    # 符号反転
    print(-x)

    # 冪乗
    print(x ** y)

    # 複数の値の比較演算
    a = 100
    b = 200
    c = 300
    print(a < b < c) # a < b and b < cと書かなくて良い
    
# bool
def bool_type():
    a = True
    b = False

    # aかつb
    x = a and b
    print(x)

    # aまたはb
    y = a and b
    print(y)
    
    # aではない
    z = not a
    print(z)

# float
def float_type():
    a = 0.1
    b = 1.7
    print(a + b)

    c = 1e-1
    d = 1.7e+0
    print(c + d)

    # 無限大を表現できる
    e = float('inf')
    print(e)

    # 非数(nan)
    print(e + -e)

# str
def str_type():
    text1 = 'ABC'
    print(text1)

    text2 = "ABC"
    print(text2)

    text3 = """
ABC
DEF
GHI
"""
    print(text3)

    # エスケープ
    text4 = 'I\'m pythonista'
    print(text4)

    # 改行のエスケープ
    text5 = 'aaa\
bbb'
    print(text5)

    # 文字列の連結
    text6 = 'aaa'
    text7 = 'bbb'
    text8 = text6 + text7
    print(text8)

    # エスケープシーケンスの無効化
    text9 = r'aaa\nbbb\nccc'
    print(text9)

    # 文字数
    text10 = 'abcdefghijklmn'
    print(len(text10))

# list
def list_type():
    # 数値のリスト
    a = [1, 5, 7]

    # 数値と文字列のリスト
    b = [1, 'text', 100]

    # 空のリスト
    c = []

    # 文字列からリスト生成
    d = list('sample')
    print(d)

    # リストの要素参照
    e = ['りんご', 'みかん', 'バナナ']
    print(e[0])
    print(e[1])
    print(e[2])

    # リストの更新
    e[1] = 'いちご'
    print(e[1])

    # スライス構文
    f = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f[0:3])       # 0番目から2番目まで
    print(f[4:5])       # 4番目のみ
    print(f[0:11:2])    # 0番目から10番目まで2つ飛ばしで
    print(f[0:-1])      # マイナス表記(f[0:10]と同じ)

    # リストの要素数
    print(len(f))

show_keyword()
int_type()
bool_type()
float_type()
str_type()
list_type()