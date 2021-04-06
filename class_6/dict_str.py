user_input = input('Input a string: ')


def str_char(str):
    '''that takes a string as input and returns a dictionary in which the keys will be
individual characters from the specified strings, and as values, the number of occurrences of the
specific character in the string'''

    return {k : k.count(k) for k in str}


print(str_char(user_input))