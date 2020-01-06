'''
Given 2 arrays, create a fucntion that let's a user know
(True/False) whether these two arrays contain any common items
'''

#using dictionaries to see if there is a common item
def containCommonItems(list1, list2):
    dict = {}                    #create dict
    for i in range(len(list1)): 
        dict[list1[i]] = True    #store the first list into dict

    for e in list2:
        if dict.get(e) == True:  #use get() method since we doing know if second list has an element from first
            return True
    
    return False
  
#using sets to see if there is a common item  
def containCommonItems2(list1, list2):
    L1Set = set(list1)
    for i in list2:
        if i in L1Set:
            return True
        
    return False
    
print(containCommonItems2(['a', None, 'c', 'x'], ['z', None, 'i']))
print(containCommonItems2(['a', 'b', 'c', 'x'], ['z', 'y', 'a']))
print(containCommonItems2(['a', 'b', 'c', 'x'], ['z', 'y', 'x']))