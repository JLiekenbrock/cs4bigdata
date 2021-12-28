import timeit

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

def generate(_items: [int]) -> [[int]]:
    res = [[]]
    for item in _items:
        new_set = [r+[item] for r in res]
        res.extend(new_set)
    yield res

#1:
def optimize_scrum_tasks(_cost_constraint: int) -> (int, int, [int]):
    _sol_benefit, _sol_cost, _solution = 0, 0, []
    possible_solutions = generate([ i for i in range(len(scrum_tasks))])
    for solution in possible_solutions:
        cost = sum([scrum_tasks[task][2] for task in solution])
        if cost <= _cost_constraint:
            benefit = sum([scrum_tasks[task][1] for task in solution])
            if benefit > _sol_benefit:
                _sol_benefit = benefit
                _sol_cost = cost
                _solution = solution
    return _sol_benefit, _sol_cost, _solution

for cost_limit in [9, 10, 20, 30, 40, 50, 60, 100, 150, 200, 1000]:
    sol = optimize_scrum_tasks(cost_limit)
    print('cost_constraint:' + str(cost_limit).rjust(5) + \
    ', b/c: ' + str(str(sol[0]) + '/' + str(sol[1])).rjust(7) + \
    ', solution: ' + str(sol[2]))

#3 
print('''
    The optimized solution yields a total benefit of 375 with total costs of 170. 
    The initial solution only generated a benefit of 180. 
''')

#4
new_tasks = [
    ('id_578', 15, 60, 'feat #5206: ...'),
    ('id_390', 20, 20, 'feat #9524: ...'),
    ('id_340', 40, 10, 'feat #4954: ...'),
    ('id_234',100, 30, 'bug 2893: ...'),
    ('id_193', 50, 10, 'bug #3466: ...'),
    ('id_450', 40, 20, 'bug #3205: ...'),
    ('id_344', 60, 30, 'feat #4503: ...')
    ]
scrum_tasks.extend(new_tasks)

opt = optimize_scrum_tasks(200)
print("The new optimal solution creates", opt[0], "benefit at", opt[1],"cost and contains these tasks: ",opt[2])

#5 
new_tasks = [
    ('id_564', 20, 20, 'feat #7422: ...'),
    ('id_412', 30, 10, 'bug #4566: ...')
]
scrum_tasks.extend(new_tasks)

opt = optimize_scrum_tasks(200)
print("The new optimal solution creates", opt[0], "benefit at", opt[1],"cost and contains these tasks: ",opt[2])

print("The complexity of the algorithm is exponential. This means that the execution time will increase significantly with each added task.")

#6
print('''
    The solutions space for 11 tasks contains 2^11 = 2048 possible solutions. The solutions space for 20 is 2^20 = 1048576 possible solutions.
    This is an increase of 2^20-2^11 = 1048576-2048 = 1046528 possible solutions.
    ''')