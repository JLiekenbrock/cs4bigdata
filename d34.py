#D3
scrum_tasks = [
    # task_id, benefit, cost estimates, description
        ('id_428', 50, 10, 'bug #3150: left column alignment broken'),
        ('id_528', 25, 20, 'bug #4254: logout leaves hourglass on screen'),
        ('id_644', 30, 10, 'idea: move shopping cart icon to the right'),
        ('id_222', 15, 80, 'investigate #4259: logout slow'),
        ('id_680', 30, 60, 'feat #4386: color scheme for fall skin'),
        ('id_220', 30, 20, 'feat #4255: internationalize for Spanish'),
        ('id_421', 30, 20, 'feat #4256: internationalize for Russian'),
        ('id_682',120, 30, 'bug #4002: empty password crashes backend'),
        ('id_368', 30, 10, 'fix comments in optimization module'),
        ('id_932', 30, 25, 'bug #4846: exception thrown for empty field'),
        ('id_387', 30, 25, 'feat #8427: new option to change color scheme'),
    ]

#1 
print('''
    Highest benefit is 170. Task #222 and #680 should be avoided. 
    All other tasks sum up to a cost of 170. Replacing the other tasks with the two left expensive ones would make no senese, as they provide poor benefits even.
    One could only think of replacing #528 with #680 from benefit point of view, however that would add up to costs of 210 and is thus not feasible.
''')

#2 
print('''
    I would consider an approach that uses the cost/benefit ratio. 
    From that point of view #222 and #680 are easily identified as 'bad tasks'.
    Then i would add up the remaining tasks and see how much capacity is left, and then i would start to think of optimizing the left capacity by identifying items that might be switched from the selection.
''')

#3 
print('''
    It doesn't condense well into an algorithm. If all tasks have a rather similiar cost/benefit ratio it does not work well, as there are many candidates for switching.
''')

#4
print('''
    It is a powerset. The solution is a subset of the original set, while the powerset is the set of all subsets, which are all possible solutions. Permutation is about changing the order whithin a set, which does not play a role here at all.
''')

#5
def generate(_items: [int]) -> [[int]]:
    res = [[]]
    for item in _items:
        new_set = [r+[item] for r in res]
        res.extend(new_set)
    return res
    
#6 
print('''
    The function first creates an array that only contains an empty array for the solution.
    Then it loops through the original list.
    FOr each element in the list a new list is created using a list comprehension.
    This list comprehension adds the current element of the original list and adds it to all elements so far in the power set. 
    The new_set is then merged with the result set. 
''')

#7 
print('''
    The given set has 11 elements. The powerset contains 2^11 = 2048 elements.
    In general a Powerset consists of 2^n elements, where n is the number of elements in the original set.
''')

#8
print('''
    Yield will return a generator object whereas return will return the power set itself.
    In case of return the whole powerset will be stored in memory once the function is called.
    Yield will only create the generator object but the power set will not be stored, but generated on the fly.
    The generator can be iterated using the next() function or via printing it or triggering the generator by "converting" it to a list.
''')