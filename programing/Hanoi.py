# -*- coding:UTF-8 -*-

def hanoi(a, b, c, n):
    if n == 1:
        print a, '->', c
    else:
        hanoi(a, c, b, n-1)
        print a, '->', c
        hanoi(b, a, c, n-1)
n = int(raw_input(u'请输入汉诺塔的层数：'))
print hanoi('a', 'b', 'c', n)