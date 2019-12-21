'''
Given 2 arrays, create a fucntion that let's a user know
(True/False) whether these two arrays contain any common items
'''

def containCommonItems(list1, list2):
    dict = {}                    #create dict
    for i in range(len(list1)): 
        dict[list1[i]] = True    #store the first list into dict

    for e in list2:
        if dict.get(e) == True:  #use get() method since we doing know if second list has an element from first
            return True
    
    return False
    
print(containCommonItems(['a', None, 'c', 'x'], ['z', None, 'i']))
print(containCommonItems(['a', 'b', 'c', 'x'], ['z', 'y', 'a']))
print(containCommonItems(['a', 'b', 'c', 'x'], ['z', 'y', 'x']))