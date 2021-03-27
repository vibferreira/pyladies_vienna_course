from random import randrange

dice = [1,1,1,1]

def dice_game(dice):
    """ Checks in a list of players who needed the least number of tries to reach the number 6 in a dice\n
    dice = list of players (have to be initiated with any number != than 6)
    """
    lst = [[],[],[],[]]
    for i in range(len(dice)):
        while dice[i] != 6:
            dice[i] = randrange(1,7)
            lst[i].append(dice[i])

    list_len = [len(i) for i in lst]

    # list_len = [] 
    # for i in lst:
    #     list_len.append(len(i))

    print(lst,'\n',list_len)
    min_winner = min(list_len)
    print('The smalles number of tries was {}'.format(min_winner))
    # print('The player with the smallest number of tries is {} with {}'.format(min_winner)) # I dunno how to access the index of the winner


dice_game(dice)


### try to use recursion