#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：王安勇
日期：2020/11/20
"""

import random



# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """
    if name=="石头":
       return 0
    elif name=="史波克":
       return 1
    elif name=="纸":
       return 2
    elif name=="蜥蜴":
       return 3
    elif name=="剪刀":
       return 4

def number_to_name(number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if number==0:
       return "石头"
    elif number==1:
        return "史波克"
    elif number==2:
        return "纸"
    elif number==3:
        return "蜥蜴"
    elif number==4:
        return "剪刀"
def rpsls(player_choice):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果

    """
    player_choice_number=name_to_number(player_choice)
    comp_number=random.randrange(0,5)
    computer=number_to_name(comp_number)
    print("--------")
    print("您的选择为:%s"%(player_choice))
    print("计算机的选择为:%s"%(computer))
    if player_choice_number==0:
        if comp_number==4 or comp_number==3:
            print("您赢了")
        elif comp_number==0:
            print("您和计算机出的一样呢")
        else:
            print("计算机赢了")
    if player_choice_number == 1:
        if comp_number==4 or comp_number==0:
            print("您赢了")
        elif comp_number==1:
            print("您和计算机出的一样呢")
        else:
            print("计算机赢了")
    if player_choice_number == 2:
        if comp_number ==1 or comp_number == 0:
            print("您赢了")
        elif comp_number==2:
            print("您和计算机出的一样呢")
        else:
            print("计算机赢了")
    if player_choice_number == 3:
        if comp_number ==1 or comp_number == 2:
            print("您赢了")
        elif comp_number==3:
            print("您和计算机出的一样呢")
        else:
            print("计算机赢了")
    if player_choice_number == 4:
        if comp_number ==2 or comp_number == 3:
            print("您赢了")
        elif comp_number==4:
            print("您和计算机出的一样呢")
        else:
            print("计算机赢了")

# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
if choice_name=="石头" or choice_name=="史波克" or choice_name=="纸" or choice_name=="蜥蜴" or choice_name=="剪刀":
    rpsls(choice_name)
else:
    print("Error: No Correct Name")
