pets = ['dog', 'cat', 'rabbit', 'snake']

def less_than_five_words(list):
    '''returns the elements with less than 5 characaters
    list = list of str elements'''
    less_than_five = [pet for pet in list if len(pet) < 5]
    return less_than_five

print(less_than_five_words(pets))


def starts_with_d(list):
    '''returns the words that starts with the letter d
    list = list of str elements'''
    starts_with_d = [pet for pet in list if pet.startswith('d')]
    return starts_with_d

print(starts_with_d(pets))

def word_in_list(word, list):
    '''detecs if a word is on the list
    word = word that will be checked
    list = list of str elements'''
    word_in_list = [True if word in list else False]
    return word_in_list

print(word_in_list('dog', pets))


