user_input = int(input('Input the size of the dictionary: '))

def dict_squared(num):
    '''creates and returns a dictionary for the specified number n, where the
    keys will be numbers from 1 to n and the values will be respective numbers n2 - squared'''

    return {i : i**2 for i in range(1,num+1)}
print(dict_squared(user_input))
dic=dict_squared(user_input)  

def sum_key_values(dict):
    ''' gets a dictionary as argument and returns the sum of all keys and sum of
    all values in the dictionary received. Use as input the dictionary created in previous exercise.'''

    sum_keys = sum(dict.keys())
    sum_values = sum(dict.values())

    return f'the sum of the keys is {sum_keys} and the sum of the values is {sum_values}'

print(sum_key_values(dic))