# -*- coding:utf-8 -*-

while(1):
    grade = float(raw_input(u'请输入您的分数（退出请按0）：'))
    if grade == 0:
        break
    elif grade >= 90 and grade <= 100:
        print 'A'
    elif grade >= 70 and grade < 90:
        print 'B'
    elif grade >= 60 and grade < 70:
        print 'C'
    elif grade > 0 and grade < 60:
        print 'D'
    else:
        print 'Invalid score'