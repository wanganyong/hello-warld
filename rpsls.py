#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�������
���ڣ�2020/11/20
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if name=="ʯͷ":
       return 0
    elif name=="ʷ����":
       return 1
    elif name=="ֽ":
       return 2
    elif name=="����":
       return 3
    elif name=="����":
       return 4

def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number==0:
       return "ʯͷ"
    elif number==1:
        return "ʷ����"
    elif number==2:
        return "ֽ"
    elif number==3:
        return "����"
    elif number==4:
        return "����"
def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
    player_choice_number=name_to_number(player_choice)
    comp_number=random.randrange(0,5)
    computer=number_to_name(comp_number)
    print("--------")
    print("����ѡ��Ϊ:%s"%(player_choice))
    print("�������ѡ��Ϊ:%s"%(computer))
    if player_choice_number==0:
        if comp_number==4 or comp_number==3:
            print("��Ӯ��")
        elif comp_number==0:
            print("���ͼ��������һ����")
        else:
            print("�����Ӯ��")
    if player_choice_number == 1:
        if comp_number==4 or comp_number==0:
            print("��Ӯ��")
        elif comp_number==1:
            print("���ͼ��������һ����")
        else:
            print("�����Ӯ��")
    if player_choice_number == 2:
        if comp_number ==1 or comp_number == 0:
            print("��Ӯ��")
        elif comp_number==2:
            print("���ͼ��������һ����")
        else:
            print("�����Ӯ��")
    if player_choice_number == 3:
        if comp_number ==1 or comp_number == 2:
            print("��Ӯ��")
        elif comp_number==3:
            print("���ͼ��������һ����")
        else:
            print("�����Ӯ��")
    if player_choice_number == 4:
        if comp_number ==2 or comp_number == 3:
            print("��Ӯ��")
        elif comp_number==4:
            print("���ͼ��������һ����")
        else:
            print("�����Ӯ��")

# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
if choice_name=="ʯͷ" or choice_name=="ʷ����" or choice_name=="ֽ" or choice_name=="����" or choice_name=="����":
    rpsls(choice_name)
else:
    print("Error: No Correct Name")
