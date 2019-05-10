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
no1 = texts.find('대표 구성원 정보')
part1 = texts[no1+9:]
no2 = part1.find('구성원 정보')
no3 = part1.find('커뮤니티 및 활동 소개')
part2 = part1[no2:no3]
part1 = texts[no1:]

c_index2 = part1.find('커뮤니티 규모')
c_text = part1[:c_index2]

for c in c_text.split('굈'):
    if len(c) > 1 : community_name = c.strip()

c_size_index = texts.find('커뮤니티 규모')
c_size_index2 = texts.find('?동분야')
c_text2 = texts[c_size_index+7:c_size_index2]

end_flag = part1.find('역할')
while end_flag>0:
    part1 = part1[end_flag + 2:]
    people = dict()
    age_index = part1.find('나이')
    gender_index = part1.find('성별')
    phone_index = part1.find('휴대전화')
    email_index = part1.find('이메일')
    address_index = part1.find("주소")
    next_index = part1.find('주소굈굈역할')

    flag = False
    for a in part1[age_index+2:gender_index].split('굈'):
        a = a.split('굈')[0].strip()
        if a == '만  (      )세': break
        if len(a):
            try:
                a= a.split('(')[1].split(')')[0].strip()
            finally:
                people['age'] = a
                break

    for a in part1[gender_index+2:phone_index].split('굈'):
        print ((a == '여') or (a == '남'))
        if a == '성명': break
        if (a == '여') or (a == '남') :
            people['gender'] = a
            gender_index = gender_index + 3
            print(a)
            break

    for n in part1[gender_index:phone_index].split('굈'):
        n = n.split('굈')[0].strip()
        if n == '이메일':break
        if len(n)>1:
            people['name'] = n
            break

    for a in part1[phone_index+4:email_index].split('굈'):
        a = a.split('굈')[0].strip()
        if a.startswith('0') :
            people['phone'] = a
            break


    for a in part1[email_index+3:address_index].split('굈'):
        a = a.strip()
        if'@' in a :
            people['email'] = a
            break

    for a in part1[address_index+2:no2].split('굈'):
        a = a.strip()
        if a == '역할': continue
        if len(a.split()):
            people['address'] = a
            break
        if a =='대표/팀원 선택': break

    end_flag = part1[end_flag+2:].find('주소굚역할')
    print(people)