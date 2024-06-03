# -*- coding: euc-kr -*-
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 하나만 출력합니다
print("# 하나만 출력합니다")
print("Hello Python Programming...!")
print("========")

# 여러 개를 출력합니다
print("# 여러 개를 출력합니다")
print(10, 20, 30, 40, 50)
print("안녕하세요", "저는", "파이썬을", "오랜만에 해요")
print("========")

# type 확인
print("# type 확인")
print(type('하이'))
print(type("안녕하세요"))
print(type(123))
print("========")

# 반복 출력
print("# 반복 출력")
print("세 번 출력!," * 3)

# 문자열 출력
print("# 문자열 출력")
hello = "안녕하세요"
print(hello[2:5])#안[0], 녕[1], 하[2], 세[3], 요[4]
print("========")
# 문자열 길이 출력
print("문자열 길이 출력")
print("이것의 길이는?")
print(len("이것의 길이는?"))
