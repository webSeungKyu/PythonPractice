# -*- coding: euc-kr -*-
import secrets
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 비교 연산자
print(True)
print(False)
print(10==10)
print(10=="10")
print("가나" > "가가")
x = 25
print(10 < x < 30)

if x > 10:
    print("x는 10보다 크다")
else:
    print("x는 10보다 크지 않다")

if x == 30:
    print("x는 30입니다")
elif x >= 25:
    print("x는 25보다 크거나 같습니다")
else:
    print("x는 25보다 작습니다")

#날짜/시간 관련 기능
import datetime

now = datetime.datetime.now()
print(now)
print("현재 순서대로 년, 월, 일, 시, 분, 초")
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")
print("{}년 {}월 {}일 {}시 {}분 {}초".format(now.year, now.month, now.day, now.hour, now.minute, now.second))
