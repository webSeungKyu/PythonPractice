# -*- coding: euc-kr -*-
import secrets
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# �� ������
print(True)
print(False)
print(10==10)
print(10=="10")
print("����" > "����")
x = 25
print(10 < x < 30)

if x > 10:
    print("x�� 10���� ũ��")
else:
    print("x�� 10���� ũ�� �ʴ�")

if x == 30:
    print("x�� 30�Դϴ�")
elif x >= 25:
    print("x�� 25���� ũ�ų� �����ϴ�")
else:
    print("x�� 25���� �۽��ϴ�")

#��¥/�ð� ���� ���
import datetime

now = datetime.datetime.now()
print(now)
print("���� ������� ��, ��, ��, ��, ��, ��")
print(now.year, "��")
print(now.month, "��")
print(now.day, "��")
print(now.hour, "��")
print(now.minute, "��")
print(now.second, "��")
print("{}�� {}�� {}�� {}�� {}�� {}��".format(now.year, now.month, now.day, now.hour, now.minute, now.second))
