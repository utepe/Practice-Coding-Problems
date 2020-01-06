'''
Implement an autocomplete system.
That is, given a query string s and 
a set of all possible query strings,
return all strings in the set that have s as a prefix
'''

def possibleCompletions(s, strSet):
    containsPrefix = set()
    size = len(s)
    for i in strSet:
        if i[:size] == s:
            containsPrefix.add(i)         
    return containsPrefix

if __name__ == '__main__':
    print(possibleCompletions('de', {"dog", "deer", "deal"}))
    print(possibleCompletions('ca', {"cat", "car", "cer"}))
    print(possibleCompletions("ae", {"cat", "car", "cer"}))
    print(possibleCompletions("ae", {}))