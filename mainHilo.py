import random
'''dice123'''
def dice():
    '''dice'''
    dice1 = [1, 2, 3, 4, 5, 6]
    dice2 = [1, 2, 3, 4, 5, 6]
    dice3 = [1, 2, 3, 4, 5, 6]
    result_num = (random.choice(dice1))+(random.choice(dice2))+(random.choice(dice3))
    return result_num
'''condition'''
def condition1():
    '''condition'''
    dice_result1 = dice()
    if dice_result1 >= 12:   #แต้มสูง 12-18
        print("HIGH")
    elif dice_result1 == 11: #11 ไฮโล
        print("11 HILO")
    else:                   #แต้มต่ำ 3-10
        print("LOW")
condition1()
