
dic = {'name': ['Vitoria','Carolina', 'Pedro'],
'age': [24,19,65]}

def key_values_ind_lines(dict):
    '''that lists the content of the dictionary (the keys and their associated values) on
    individual lines '''
    for key, value in dict.items():
        print(key, ':', value)

key_values_ind_lines(dic)