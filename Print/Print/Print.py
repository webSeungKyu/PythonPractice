# -*- coding: euc-kr -*-
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# �ϳ��� ����մϴ�
print("# �ϳ��� ����մϴ�")
print("Hello Python Programming...!")
print("========")

# ���� ���� ����մϴ�
print("# ���� ���� ����մϴ�")
print(10, 20, 30, 40, 50)
print("�ȳ��ϼ���", "����", "���̽���", "�������� �ؿ�")
print("========")

# type Ȯ��
print("# type Ȯ��")
print(type('����'))
print(type("�ȳ��ϼ���"))
print(type(123))
print("========")

# �ݺ� ���
print("# �ݺ� ���")
print("�� �� ���!," * 3)

# ���ڿ� ���
print("# ���ڿ� ���")
hello = "�ȳ��ϼ���"
print(hello[2:5])#��[0], ��[1], ��[2], ��[3], ��[4]
print("========")
# ���ڿ� ���� ���
print("���ڿ� ���� ���")
print("�̰��� ���̴�?")
print(len("�̰��� ���̴�?"))
