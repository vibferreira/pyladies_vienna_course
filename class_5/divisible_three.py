#print numbers divisible per 3 or 5 in a range from 0 to 100 

def div_three_five(seq_size):
    """Check if a number is divisble by 3 or 5 
    within a sequence and sum all the numbers that meet this condition\n
    seq_size = size of sequence """

    lst = []

    for i in range(seq_size):
        if(i%3 == 0) or (i%5 == 0):
            lst.append(i)
    print(sum(lst))

div_three_five(100) 
    