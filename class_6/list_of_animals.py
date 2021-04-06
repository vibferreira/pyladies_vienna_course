mammals = ['cat', 'dog', 'cow', 'whale','dolphin']
aquatic_animals = ['whale','shark','clownfish','dolphin']

def list_both (list1,list2):
    both_lists = [both for both in list1 if both in list2] 
    return both_lists 

print(list_both(mammals,aquatic_animals))

def only_first_list (list1,list2):
    first_list = [both for both in list1 if both not in list2] 
    return first_list 

print(only_first_list(mammals,aquatic_animals))

def only_second_list (list1,list2):
    second_list = [both for both in list2 if both not in list1] 
    return second_list 

print(only_second_list(mammals,aquatic_animals))
