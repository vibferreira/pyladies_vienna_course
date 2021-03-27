
range_user = int(input("Input the size of the range of numbers: "))

list_user = list(range(range_user)) #starts from the first prime num

prime_list = [] #it will store the prime numbers retrieved from the loop 

def prime_number(user_list):
    """Prime_number returns a list of prime numbers in a range defined by the user\n
   user_list = range defined by the user"""

    for num in range (len(user_list)): # this range returns the size of the list
        num = user_list[num]
        for i in range (2, num): # it starts at 2 in order to check if num is divided for 2 onwards -- not working!!!
            # print(i)
            if not(num % i == 0):
                final_prime_list = prime_list.append(num)
    return 
    final_prime_list
             
print(prime_number(list_user))


# first try

# for num in list_user: # num is the number in the range I wanna check if it is prime
#     num = list_user[num]
#     for i in list_user: # it starts at 2 because a prime num can only be divided by one and itself
#         if num % list_user[i] == 0:
#             break
# else:
#     prime_list = prime_list.append(num)

# print(prime_list)

#how to make the for loop check if the number is prime for each number

