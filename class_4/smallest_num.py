"""Solution 1""" 

# list_of_inputs = []
# for i in range(5):
#    num = float(input("Input a number: "))
#    list_of_inputs.append(num)

# print("The smallest number is: ", min(list_of_inputs))

"""Solution 2"""
num1 = float(input("Input the first number: "))
num2 = float(input("Input the second number: "))
num3 = float(input("Input the third number: "))
num4 = float(input("Input the forth number: "))
num5 = float(input("Input the fifth number: "))

smallest_num = 0

"""working code"""
# if num1 <= num2:
#     if num1 <= num3:
#         if num1 <= num4:
#             smallest_num = num1
#     elif num3 <= num1:
#         if num3 <= num4:
#             smallest_num = num3
#         else:
#             smallest_num = num4
# elif num2 <= num1:
#     if num2 <= num3:
#         if num2 <= num4:
#             smallest_num = num2
#     elif num3 <= num2:
#         if num3 <= num4:
#             smallest_num = num3
#         else:
#             smallest_num = num4


"""not working code for num4 and num5"""
if num1 <= num2:
    if num1 <= num3:
        if num1 <= num4:
            if num1 <= num5:
                smallest_num = num1
    elif num3 <= num1:
        if num3 <= num4:
            if num3 <= num5:
                smallest_num = num3
    elif num4 <= num1:
        if num4 <= num5:
            smallest_num = num4
        else:
            smallest_num = num5
elif num2 <= num1:
    if num2 <= num3:
        if num2 <= num4:
            if num2 <= num5:
                smallest_num = num2
    elif num3 <= num2:
        if num3 <= num4:
            if num3 <= num5:
                smallest_num = num3
    elif num4 <= num2:
        if num4 <= num5:
            smallest_num = num4
        else:
            smallest_num = num5

print("The smallest number is ", smallest_num)






