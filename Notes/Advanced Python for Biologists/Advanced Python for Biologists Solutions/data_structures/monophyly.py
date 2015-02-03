# define the tree to use for testing
tree = tree = ['dog', ['raccoon','bear'], [['sea_lion','seal'],['monkey','cat'], 'weasel']]

# a function to test if a given list contains a target element
def contains(my_list, target): 
    result = False 
    for element in my_list: 
        # for elements that are lists, recursively check if they contain the target element
        if isinstance(element, list): 
            if contains(element, target): 
                result = True 
        # for elements that aren't lists, check if they are the target element
        else: 
            if element == target: 
                result = True 
    return result 

# function to test if any sublists of a nested list support the tree ((taxon1,taxon2),taxon3)
def are_closely_related(my_list, taxon1, taxon2, taxon3):
    result = False
    # if this list contains taxon1 and taxon2 but not taxon3 then it satisfies the test
    if (contains(my_list, taxon1) 
    and contains(my_list, taxon2) 
    and not contains(my_list, taxon3)):
        result = True
    # see if any sublists satisfy the test by calling the function recursively
    for sublist in my_list:
        if isinstance(sublist, list):
            if are_closely_related(sublist, taxon1, taxon2, taxon3):
                result = True
    return result

