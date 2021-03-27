import numpy as np

user_seq = int(input("Input the size of a sequence: "))

def lcm (seq):
    """Calculates the least divisible number within a list\n
    seq = list of numbers"""
    lst = list(range(1, seq+1))
    lcm = np.lcm.reduce(lst)
    print(lcm)

lcm(user_seq)