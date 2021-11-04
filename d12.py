import sys
orig_stdout = sys.stdout
f = open('output.txt', 'w')
sys.stdout = f
# 1

def is_sorted(_list: [], _log: bool = False) -> bool:
    l = len(_list)
    # In dubio pro reo
    s = True
    if l>= 2:
        s = _list[0] <= _list[1]
        if _log:
            print(f"{_list[0]} < {_list[1]} ->  {s}")
        if s and l > 2 :
            return is_sorted(_list[1:], _log)
    return s

# 2
print("2.) What is the “time‐complexity” of your function (how many comparisons are needed for n‐elements in the input list):")
print("a : 1")
print("b : n-1")
print("b : (n-1)/2")

# 3+4
numbers = [
    [1, 2, 3, 0, 4, 5, 6, 7, 8, 9],
    [4, 8, 12, 12, 24, 36],
    [], [2], [1, 2], [2, 1]
]
print("\n3+4:")

for n in numbers:
    print(str(is_sorted(n,_log=True)) + '\t<-- ' + str(n))

# 5
import C1_us_name_stats as ns 

# 6
print("\n6:")

def find_name(_name: str, _list: []) -> int:
    s = [ i for i,x in enumerate(ns.us_names_top1000) if x == _name]
    return s[0] if s else -1

name_list = ns.us_names_top1000
name_freq = ns.us_name_freq_top1000
names = ['Smith', 'Mendoza', 'Rodriguez', 'Abbott', 'Blokes', 'Brewer',
'Vang', 'Zimmerman', 'Bailey']

for n in names:
    i = find_name(n, name_list)
    print(str(i) + '\t<-- ' + str(n), end='')
    print('\t\t--> freq: ' + str(name_freq[i]) if i >= 0 else "")

#7 
print("\n7:")

print("What is the time‐complexity of your function (how many comparisons are needed for n‐elements in the input list of names):")
print("a : 1")
print("b : n-1")
print("b : (n-1)/2")

sys.stdout = orig_stdout
f.close()
