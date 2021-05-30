
from pet import pets
# pets = ['dog', 'cat', 'rabbit', 'snake']

#sorting list alphabetically
#print(pets.sort())
# print(pets)

#sorting alphabetically ignoring the first letter 
def sort_second(list):
    ''' Sorts a list alphabetically ignoring the first letter
    list = list of str elements'''
    list = [list[i][1:] for i in range(len(list))]
    list.sort()
    return list

print(sort_second(pets))

# print(pets[0][1:])
# pets = [pets[i][1:] for i in range(len(pets))]
# pets.sort()
# print(pets)