# -*- coding: euc-kr -*-
from pickle import INST
import sys
import io
from turtle import st

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#리스트
list_a = [1, 2, 3]

#리스트에 ! 문자를 넣고 있는지 확인
list_a.append("!")
isTrue = "!" in list_a
print(isTrue)


list_a.insert(3, 4)

#리스트에 마지막 배열 제거 후 다시 확인
list_a.pop()
isTrue = "!" in list_a
print(isTrue)

print("list_a = ", list_a)
print("==============")
#반복문 확인
for i in list_a:
    print(i)
    
hello = "안녕하세요"
for i in hello:
    print("-", i)
    
    print("--------")
    
print("==============")

#딕셔너리
movie = {
    "name":"영화 이름",
    "type": "영화 타입",
    }
print(movie)
print(movie["name"])
print(movie["type"])
print("--------")
names = {
    "first": ["김", "나", "박", "이"],
    "end": ["치", "방", "수", "화수"]
    }

print(names)
print("성(first) 목록 : ", names["first"])
print("이름(end) 목록 :", names["end"])

if "화수" in names["end"]:
    print("names에 {}가 있습니다".format('"화수"'))

first = names.get("first")
print(first)
end = names.get("end")
print(end)

num = 0
#파이썬에는 증감연산자가 없네..
for i in names["end"]:

    if i == "화수":
        print("{}회 만에 화수 발견".format(num))
        num += 1
    else:
        print("화수 미발견.. / 현재 회차 : {}".format(num))
        num += 1

#반복문
for i in range(0, 11):
    print(i)
    
print("==============")
pets = [
    {"name":"구름", "age": 5},
    {"name":"초코", "age": 3},
    {"name":"아지", "age": 1},
    {"name":"호랑이", "age": 1}
    ]

print("#애완 동물들")
for i in pets:
    print(i.get("name"), "{}살".format(i.get("age")))

print("==============")
numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}

for i in numbers:
    if counter.get(i) == None:
        counter[i] = 1
    else:
        counter[i] = counter.get(i) + 1
    

print(counter)
print(type(counter is dict))
print(type(counter) is dict)
print("==============")
character = {
    "name": "기사",
    "level": 12,
    "items":{
        "sword": "불꽃의 검",
        "armor": "풀플레이트"
        },
    "skill": ["베기", "세게 베기", "아주 세게 베기"]    
    }

for key in character:
    print("{} :".format(key), character[key])
    

print("==============")

star = ""
for i in range(0, 8):
    print(star)
    star = star + "*"
    
whileI = 0
while whileI < 10:
    whileI = whileI + 1
    print("{}번째 반복입니다".format(whileI))
    
whileJ = 0
while True:
    whileJ += 1
    print("{}번째 반복입니다".format(whileJ))
    if whileJ == 28:
        print("28..?")
    elif whileJ == 50:
        break