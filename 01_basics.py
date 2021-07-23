'''
Pythonの基本
'''
# print関数
x = 1
y = 2
z = 3

# 区切り文字を指定できる
print(x, y, z, sep=',')

# 終端文字を指定できる(改行以外を指定できる)
print('---', end='')
print(x, end='')
print('---')

# モジュールのインポート
import math as m
from datetime import date as d
