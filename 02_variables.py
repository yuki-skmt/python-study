'''
変数
'''

from keyword import kwlist

# 予約語一覧
def show_keyword():
    print(kwlist)

show_keyword()

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

int_type()
    
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

bool_type()

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

float_type()

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

str_type()

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

    # リストへの要素追加
    g = ['りんご', 'みかん', 'バナナ']
    g.append('いちご')
    print(g)

    # リストへの要素挿入
    g.insert(0, 'オレンジ')
    print(g)

    # リストの要素削除(del)
    del g[2]
    print(g)

    # リストの要素削除(remove)
    g.remove('オレンジ')
    print(g)

    # リストの要素取り出し(pop)
    h = g.pop(2)
    print(g)
    print(h)

    # リストの要素検索
    i = g.index('バナナ')
    print(i)

    # リストのアンパック
    j = [100, 200, 300]
    k, l, m = j
    print(k)
    print(l)
    print(m)

list_type()

# tuple
def tuple_type():
    t1 = ()
    t2 = (1, )  # 要素が1つだけのタプルを使用する場合、末尾にカンマ必須
    t3 = (1, 2)

    # タプルへの変換
    t4 = tuple([1, 2, 3])
    print(t4)

    # タプルの要素参照、要素数取得、アンパックはリストと同じため省略

    # 要素の入れ替え
    # (内部的にはタプル化してアンパックしている)
    x = 100
    y = 200
    x, y = y, x
    print(x)
    print(y)

tuple_type()

# range
def range_type():
    r1 = range(4)
    r2 = range(4, 7)
    r3 = range(3, 10, 2)
    r4 = range(10, 6, -1)
    print(list(r1))
    print(list(r2))
    print(list(r3))
    print(list(r4))

range_type()

# set
def set_type():
    a = {1, 3, 5, 7}
    print(a)
    
    # 重複排除されたsetを生成
    b = set([1, 2, 3, 1, 2, 3])
    print(b)

    # 空のリスト
    c = set()
    print(c)

    # 追加
    c.add(8)
    print(c)

    # 重複を伴う追加はできない
    c.add(8)
    print(c)

    # 削除
    d = {1, 2, 3, 4}
    print(d)
    d.remove(3)
    print(d)

    # 全削除
    d.clear()
    print(d)

    # 存在判定
    e = {1, 2, 3, 4, 5}
    print(e)
    print(1 in e)
    print(6 in e)

    # 集合論理
    f = {'A', 'B', 'C'}
    g = {'C', 'D', 'E'}

    # 和集合
    h = f.union(g)
    print(h)

    # 差集合
    i = f.intersection(g)
    print(i)

    # 包含判定
    # サブセットか？(含まれているか)
    j = {'A', 'B'}
    k = {'A', 'B', 'C'}
    l = j.issubset(k)
    print(l)

    # スーパーセットか？(含んでいるか)
    m = k.issuperset(j)
    print(m)

set_type()

# 辞書
def dict_type():
    # 生成
    weekdays = {
        'Mon': '月',
        'Tue': '火',
        'Wed': '水',
        'Thu': '木',
        'Fri': '金',
        'Sat': '土',
        'Sun': '日',
    }
    print(weekdays)

    # 二次元リストからの変換
    weekdays_list = [
        ['Mon', '月'],
        ['Tue', '火'],
        ['Wed', '水'],
        ['Thu', '木'],
        ['Fri', '金'],
        ['Sat', '土'],
        ['Sun', '日'],
    ]
    print(dict(weekdays_list))

    # 辞書の値参照
    print(weekdays['Mon'])

    # 辞書への追加
    d = {'key1': 100}
    d['key2'] = 200
    print(d)

    # 辞書への更新
    d['key2'] = 300
    print(d)

    # 全てのキーの取り出し
    print(weekdays.keys())

    # 全ての値の取り出し
    print(weekdays.values())

    # 全てのキー・値の組み合わせの取り出し
    print(weekdays.items())

    # キーの存在判定
    print('Mon' in weekdays.keys())

    # 値の存在判定
    print('月' in weekdays.values())
    
    # キー・値の組み合わせの存在判定
    print(('Mon', '月') in weekdays.items())

    # 辞書の要素削除はリストと同じため省略

dict_type()

# bytes型
def bytes_type():
    b = bytes([0, 97, 122, 254])
    print(b)

bytes_type()