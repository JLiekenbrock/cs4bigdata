import sys
orig_stdout = sys.stdout
f = open('output.txt', 'w')
sys.stdout = f

# 1 
print("--> 1")
print("a: The built-in sort function directly sorts the list it is called on. The return value of it is none. No copies are made.")
print("b: First a shallow copy is made. Than the referenced values are sorted, thus both lists are sorted as they are actually the same one.")
print("c: The sorted function creates a shallow copy while sorting. It then returns the sorted copy.")

# 2
print("--> 2")

import C1_us_name_stats as ns 
import math
from d1 import find_name, names, name_freq

def find_name_fast(_name: str, _sortedlist: [], _lower : int = 0, _upper: int = None) -> int:

    if not _sortedlist :
        return -1
    elif _upper is None:    
        _upper = len(_sortedlist)-1

    middle = (_upper + _lower) // 2
    
    if _sortedlist[middle] == _name:
        return middle
    else:
        to_small =  _sortedlist[middle] < _name
        _lower = _lower if not to_small else middle+1 
        _upper = _upper if to_small else middle-1 
        return find_name_fast(_name,_sortedlist,_lower,_upper) if _lower <= _upper else -1


index = [-1]

def pass_index(_middlename:str, _name:str,_middle,_sortedlist):
    if index!=[-1]:
        if _middlename < _name:
            index[0] = _middle+1 
        else:
            index[1] = _middle-1
    else:
        index = [0,len(_sortedlist)-1]

pass_index("a", "b",2,["a","b","c"])


def find_name_fast(_name: str, _sortedlist: []) -> int:

    if not index:
        

    if not pass_index.values:
        middle = len(_sortedlist) // 2
    else:
        middle = sum(pass_index) // 2

    if _sortedlist[middle] == _name:
        return middle
    else:
        pass_index(_sortedlist[middle],_name.middle)
        return find_name_fast(_name,_sortedlist) if index[0] <= index[1] else -1

sorted_list = sorted(ns.us_names_top1000)

for n in names:
    i = find_name_fast(n, sorted_list)
    print(str(i) + '\t<-- ' + str(n), end='')
    print('\t\t--> freq: ' + str(name_freq[i]) if i >= 0 else "")

# 3
print("--> 3")

print("What is the “time‐complexity” of this “binary” search function (comparisons are needed for n‐elements in the input list):")
print("a : 1")
print("b : log2 n")
print("b : log2 n")

# 4
print("--> 4")

print("How many steps are needed for the list of 1000 names for cases:")

print("Linear search in unsorted list:")
print("on avg : (n-1)/2")
print("worst case: n-1")

print("Binary search in sorted list:")
print("on avg : ~10")
print("worst case: ~10")

# 5 
print("--> 5")

print("5: The most memory efficient solution would be a list or an array, where the index represents the position in the sorted list and the value corresponds to the value in the sorted list.")
print("5: To avoid searching a mapping dictionary is created on the unsorted list. The mapping dictionary has the names as keys and the original index as value.")
print("5: The index is then build by retrieving the indices from the dictionary using the sorted names.")

# 6
print("--> 6")

print("6: n")

# 7

def build_index(_list: []) -> list:
    mapping = {k: v for v, k in enumerate(ns.us_names_top1000)}
    return list(map(lambda x: mapping[x], _list))

index = build_index(sorted_list)

print("--> 8")

for n in names:
    i = find_name_fast(n, sorted_list)
    print(str(i) + '\t<-- ' + str(n), end='')
    print('\t\t--> freq: ' + str(name_freq[index[i]]) if i >= 0 else "")

# 9
print("--> 9")


print("9: A dictionary that stores the indexes in both lists would be a good alternative, because it could be very easily reversed by swapping the key and the value. The mapping dictionary i created could also be used")
print("9: A dictionary is a hash table. The hash table consists of slots which are assigned in order of entry insertion (> Python 3.7). Each slot entry is a combination of hash, key and value, implemented as C struct. Lookup costs O(1)")

sys.stdout = orig_stdout
f.close()

