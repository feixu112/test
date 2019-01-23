#!/ProgramData/Anaconda3/envs/ Python
# -*- coding:utf-8 -*-
# guess21.py
# author: cqs

import random

"""
案例：21点

-两个玩家，游戏开始先输入名字
-用字典保存每个玩家信息：姓名，获胜次数
-电脑随机产生2个数，每个玩家轮流猜1个数，与电脑随机两个数求和，最接近21点的获胜
-每轮结束显示玩家信息
-按q退出游戏
"""
print('welcome!')

target = 21

# 游戏开始先输入名字
user1 = input('第一个玩家名字：')
user2 = input('第二个玩家名字：')
print(f'玩家输入：{user1}, {user2}')

# 字典保存2个玩家相关信息
users = {
    user1:
    {'win': 0},
    user2:
    {'win': 0}
}

is_add = True
while(is_add):
    print('欢迎进入21点小游戏'.center(30, '-'))

    # PC随机产生2个数
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    # 玩家轮流猜1个数
    user1_guess = int(input(f'{user1} guess:'))
    user2_guess = int(input(f'{user2} guess:'))
    print(f'第1轮随机点数：{num1}，第2轮随机点数：{num2}')

    # 玩家数与电脑随机数求和
    user1_sum = user1_guess + num1 + num2
    user2_sum = user2_guess + num1 + num2
    print(f'{user1}总点数{user1_sum},{user2}总点数{user2_sum}')

    # 判断获胜玩家
    if abs(user1_sum - target) > abs(user2_sum - target):
        print(f'{user2} win!')
        users[user2]['win'] += 1
    else:
        print(f'{user1} win!')
        users[user1]['win'] += 1

    # 显示双方获胜情况
    m = users[user1]['win'] + users[user2]['win']
    for k, v in users.items():
        for v1, v2 in v.items():
            print(f'{m}轮，{k}累计获胜{v2}')
    is_add = input('是否继续(y/n)').strip() == 'y'
