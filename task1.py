# 1: ��������� �� ������������ �����, ��������� � ����������, ��������� � ����� 2 � �������� ��������� �� �����.
# ���� �������� ������, ���������� ��, ��������� ���� � ������������ ��������� ������.

import time

# ���� ����� �������������
number = int(input('������� ����� - '))
print(number + 2)

# 2 ��������� ����, ������������ � ������������ �����, ���� ��� �� ������ ������ 0, �� ������ 10
# ����� ����, ��� ������������ ������ ���������� �����, ��������� ��� � ������� 2 � �������� �� �����.
# ��������, ������������ ������ ����� 123, �� ��������� ���, ��� ����� ��������, � �������� � ��������� ����������. � ������� ������ ������.
# ��������, ������������ ���� 2, ��� ��������. �������� ��� � ������� 2 � ������� 4.


#start = time.perf_counter() - ������� �������

# ������� 1

# ���� ����� �������������
number = int(input('������� ����� �� 0 �� 10 - '))


while number <= 0 or number >= 10:
    print('����� ������ ���� ������ 0, �� ������ 10')
    number = int(input('������� ����� �� 0 �� 10 - '))
else:
    print('�������� ����� �� 2� ������� �������� - ', number ** 2)

#print(time.perf_counter() - start, 'var1') - ����� ������� ����������

# ������� 2

#while True:
#    number = int(input('Введите число от 0 до 10 '))
#    if number > 0 and number < 10:
#        print('�������� ����� �� 2� ������� �������� - ', number**2)
#        break
#    else:
#        print('����� ������ ���� ������ 0, �� ������ 10')

#print(time.perf_counter() - start, 'var2') - ����� ������� ����������
