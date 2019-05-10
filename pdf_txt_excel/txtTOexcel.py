#-*- coding: cp949 -*-
import glob
import pandas as pd
import sys
sys.setdefaultencoding('cp949')

filename = '22.txt'
f = open(filename, 'r')
D = dict()
community_size = 0
community_name = []
names = []
ages = []
genders = []
addresses = []
phones = []
emails = []

People = pd.DataFrame()
texts = f.read().encode('cp949').decode('cp949')
no1 = texts.find('��ǥ ������ ����')
part1 = texts[no1+9:]
no2 = part1.find('������ ����')
no3 = part1.find('Ŀ�´�Ƽ �� Ȱ�� �Ұ�')
part2 = part1[no2:no3]
part1 = texts[no1:]

c_index2 = part1.find('Ŀ�´�Ƽ �Ը�')
c_text = part1[:c_index2]

for c in c_text.split('�n'):
    if len(c) > 1 : community_name = c.strip()

c_size_index = texts.find('Ŀ�´�Ƽ �Ը�')
c_size_index2 = texts.find('?���о�')
c_text2 = texts[c_size_index+7:c_size_index2]

end_flag = part1.find('����')
while end_flag>0:
    part1 = part1[end_flag + 2:]
    people = dict()
    age_index = part1.find('����')
    gender_index = part1.find('����')
    phone_index = part1.find('�޴���ȭ')
    email_index = part1.find('�̸���')
    address_index = part1.find("�ּ�")
    next_index = part1.find('�ּ҂n�n����')

    flag = False
    for a in part1[age_index+2:gender_index].split('�n'):
        a = a.split('�n')[0].strip()
        if a == '��  (      )��': break
        if len(a):
            try:
                a= a.split('(')[1].split(')')[0].strip()
            finally:
                people['age'] = a
                break

    for a in part1[gender_index+2:phone_index].split('�n'):
        print ((a == '��') or (a == '��'))
        if a == '����': break
        if (a == '��') or (a == '��') :
            people['gender'] = a
            gender_index = gender_index + 3
            print(a)
            break

    for n in part1[gender_index:phone_index].split('�n'):
        n = n.split('�n')[0].strip()
        if n == '�̸���':break
        if len(n)>1:
            people['name'] = n
            break

    for a in part1[phone_index+4:email_index].split('�n'):
        a = a.split('�n')[0].strip()
        if a.startswith('0') :
            people['phone'] = a
            break


    for a in part1[email_index+3:address_index].split('�n'):
        a = a.strip()
        if'@' in a :
            people['email'] = a
            break

    for a in part1[address_index+2:no2].split('�n'):
        a = a.strip()
        if a == '����': continue
        if len(a.split()):
            people['address'] = a
            break
        if a =='��ǥ/���� ����': break

    end_flag = part1[end_flag+2:].find('�ּ҂�����')
    print(people)