# 2
import C1_us_name_stats as ns 
import math
from d1 import find_name, names, name_freq

def find_name_fast(_name: str, _sortedlist: [], _lower : int = 0, _upper: int = -1) -> int:
    
    if _upper == -1:    
        _upper = len(_sortedlist)-1

    middle = ( _upper + _lower)//2
    if _upper <_lower:
        return -1
    elif _sortedlist[middle] == _name:
        return middle
    elif _sortedlist[middle] < _name:
        return find_name_fast(_name,_sortedlist,middle+1,_upper)
    elif _sortedlist[middle] > _name:
        return find_name_fast(_name,_sortedlist,_lower,middle-1)

sorted_list = sorted(ns.us_names_top1000)
for n in names:
    i = find_name_fast(n, sorted_list)
    print(str(i) + '\t<-- ' + str(n), end='')
    print('\t\t--> freq: ' + str(name_freq[i]) if i >= 0 else "")

# 3
print("What is the “time‐complexity” of this “binary” search function (comparisons are needed for n‐elements in the input list):")
print("a : 1")
print("b : log2 n")
print("b : log2 n")

# 4

print("How many steps are needed for the list of 1000 names for cases:")

print("Linear search in unsorted list:")
print("on avg : (n-1)/2")
print("worst case: n-1")

print("Binary search in sorted list:")
print("on avg : ~10")
print("worst case: ~10")

# 5 
print("5: Since the index in the ordered list is represented by the index of the data strucure it is only necessary to store the associated index of the unordered list. To be able to look it up easily i would just use a plain list.")

# 6
print("6: n")

# 7
def build_index(_list: []) -> set:
    return list(map(lambda x: find_name(x,ns.us_names_top1000),_list))

# 8 
index = build_index(sorted_list)

for n in names:
    i = find_name_fast(n, sorted_list)
    print(str(i) + '\t<-- ' + str(n), end='')
    print('\t\t--> freq: ' + str(name_freq[index[i]]) if i >= 0 else "")

# 9

print("9: A dictionary that stores the indexes in both lists would be a good alternative, because it could be very easily reversed by swapping the key and the value.")
print("9: A dictionary is a hash table. The hash table consists of slots which are assigned in order of entry insertion (> Python 3.7). Each slot entry is a combination of hash, key and value, implemented as C struct. Lookup costs O(1)")