# -*- coding: euc-kr -*-
from pickle import INST
import sys
import io
from turtle import st

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#����Ʈ
list_a = [1, 2, 3]

#����Ʈ�� ! ���ڸ� �ְ� �ִ��� Ȯ��
list_a.append("!")
isTrue = "!" in list_a
print(isTrue)


list_a.insert(3, 4)

#����Ʈ�� ������ �迭 ���� �� �ٽ� Ȯ��
list_a.pop()
isTrue = "!" in list_a
print(isTrue)

print("list_a = ", list_a)
print("==============")
#�ݺ��� Ȯ��
for i in list_a:
    print(i)
    
hello = "�ȳ��ϼ���"
for i in hello:
    print("-", i)
    
    print("--------")
    
print("==============")

#��ųʸ�
movie = {
    "name":"��ȭ �̸�",
    "type": "��ȭ Ÿ��",
    }
print(movie)
print(movie["name"])
print(movie["type"])
print("--------")
names = {
    "first": ["��", "��", "��", "��"],
    "end": ["ġ", "��", "��", "ȭ��"]
    }

print(names)
print("��(first) ��� : ", names["first"])
print("�̸�(end) ��� :", names["end"])

if "ȭ��" in names["end"]:
    print("names�� {}�� �ֽ��ϴ�".format('"ȭ��"'))

first = names.get("first")
print(first)
end = names.get("end")
print(end)

num = 0
#���̽㿡�� ���������ڰ� ����..
for i in names["end"]:

    if i == "ȭ��":
        print("{}ȸ ���� ȭ�� �߰�".format(num))
        num += 1
    else:
        print("ȭ�� �̹߰�.. / ���� ȸ�� : {}".format(num))
        num += 1

#�ݺ���
for i in range(0, 11):
    print(i)
    
print("==============")
pets = [
    {"name":"����", "age": 5},
    {"name":"����", "age": 3},
    {"name":"����", "age": 1},
    {"name":"ȣ����", "age": 1}
    ]

print("#�ֿ� ������")
for i in pets:
    print(i.get("name"), "{}��".format(i.get("age")))

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
    "name": "���",
    "level": 12,
    "items":{
        "sword": "�Ҳ��� ��",
        "armor": "Ǯ�÷���Ʈ"
        },
    "skill": ["����", "���� ����", "���� ���� ����"]    
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
    print("{}��° �ݺ��Դϴ�".format(whileI))
    
whileJ = 0
while True:
    whileJ += 1
    print("{}��° �ݺ��Դϴ�".format(whileJ))
    if whileJ == 28:
        print("28..?")
    elif whileJ == 50:
        break