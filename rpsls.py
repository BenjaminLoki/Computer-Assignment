#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�Ԭ�ư�
���ڣ�2021/11/27
"""

import random#����randomģ��

# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if name == "ʯͷ":
        return 0
    if name == "ʷ����":
        return 1
    elif name == "ֽ":
        return 2
    elif name == "����":
        return 3
    elif name == "����":
        return 4
#��if��佫���ʶ�Ӧ����Ӧ�����֣���return���ؽ��

def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number == 0:
        return "ʯͷ"
    if number == 1:
        return "ʷ����"
    elif number == 2:
        return "ֽ"
    elif number == 3:
        return "����"
    elif number == 4:
        return "����"
#��if��佫���ֶ�Ӧ����Ӧ�����ʣ���return���ؽ��

def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
    print("--------")#�����߸���
    if player_choice in {"ʯͷ","ֽ","����","ʷ����","����"}:#��if�ж��������������Ӧ������
        print("����ѡ��Ϊ��%s" % player_choice)#��ʾ������������
        player_choice_number = name_to_number(player_choice)#����name_to_number��������ҵ�����ת���ɶ�Ӧ������
        comp_number = random.randint(0, 4)#��random�е�randintģ���������һ��0~4֮�������������ֵ�ɵ��Ե�����
        print("�������ѡ��Ϊ��%s" % number_to_name(comp_number))#����number_to_name���������Ե�����ת���ɶ�Ӧ�����ʣ�����ʾ
        if player_choice_number-comp_number == 0:
            print("���ͼ��������һ����")
        elif player_choice_number-comp_number in {-1,-2,3,4}:
            print("�����Ӯ��")
        elif player_choice_number-comp_number in {1,2,-3,-4}:
            print("��Ӯ��")
        #��if�ж���ҵ����ּ�ȥ�������ֵĲ������ĸ������дӶ��ж���Ӯ�Լ�ƽ�֣��ù�����ͨ��rpsls��Ϸ�Ĺ������ó��ģ�
    else:
        print("Error: No Correct Name") #����������ʲ���������ʾ����

print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()#����������ݸ�ֵ
rpsls(choice_name)#����ֵ����rpsls�����м���Ӷ���ʾ���


