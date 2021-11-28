#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：袁淦榜
日期：2021/11/27
"""

import random#导入random模块

# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """
    if name == "石头":
        return 0
    if name == "史波克":
        return 1
    elif name == "纸":
        return 2
    elif name == "蜥蜴":
        return 3
    elif name == "剪刀":
        return 4
#用if语句将名词对应到相应的数字，用return返回结果

def number_to_name(number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if number == 0:
        return "石头"
    if number == 1:
        return "史波克"
    elif number == 2:
        return "纸"
    elif number == 3:
        return "蜥蜴"
    elif number == 4:
        return "剪刀"
#用if语句将数字对应到相应的名词，用return返回结果

def rpsls(player_choice):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果

    """
    print("--------")#用虚线隔开
    if player_choice in {"石头","纸","剪刀","史波克","蜥蜴"}:#用if判定输入的名词是相应的名词
        print("您的选择为：%s" % player_choice)#显示玩家输入的名词
        player_choice_number = name_to_number(player_choice)#调用name_to_number函数将玩家的名词转化成对应的数字
        comp_number = random.randint(0, 4)#用random中的randint模块随机生成一个0~4之间的整数，并赋值成电脑的数字
        print("计算机的选择为：%s" % number_to_name(comp_number))#调用number_to_name函数将电脑的数字转化成对应的名词，并显示
        if player_choice_number-comp_number == 0:
            print("您和计算机出的一样呢")
        elif player_choice_number-comp_number in {-1,-2,3,4}:
            print("计算机赢了")
        elif player_choice_number-comp_number in {1,2,-3,-4}:
            print("您赢了")
        #用if判断玩家的数字减去电脑数字的差属于哪个数集中从而判定输赢以及平手（该规律是通过rpsls游戏的规则计算得出的）
    else:
        print("Error: No Correct Name") #若输入的名词不存在则显示错误

print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()#将输入的内容赋值
rpsls(choice_name)#将该值代入rpsls函数中计算从而显示结果


