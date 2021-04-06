
# user inputs usually comes inside or outside a function?

#user input a roman number. Each character is stored in a list.
# user_input = list(input('input a roman number:').upper())
user_input = input('input a roman number:')
# print(user_input)

def roman_to_arabic(num):
    '''converts Roman numbers to Arab numbers (integers) /n
    num = list of chars'''

    num = list(num.upper())
    dic = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M':1000}

    #stores an arabic number that corresponds to each roman letter
    arabic = [dic[i] for i in num if i in dic.keys()]

    #checks if the previous number is less than the next number, if True, multiplies it for -1
    for k in range(len(arabic)-1): #-1 so it don't past the loops length
        if arabic[k] < arabic[k+1]:
            arabic[k]*=-1
        result = sum(arabic)

    return result

print(roman_to_arabic(user_input))
