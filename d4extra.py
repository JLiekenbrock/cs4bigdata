import sys
orig_stdout = sys.stdout
f = open('d4extra.txt', 'w')
sys.stdout = f

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

benefits = [task[1] for task in scrum_tasks]
costs =  [task[2] for task in scrum_tasks]

def knapsack(_benefit: list, _cost: list, _capacity: int) -> (int, int, [int]):

    n = len(_benefit)
    w = _capacity

    dp = [ [0]*(w+1) for _ in range(n+1)]
    solution = []
    weigth = 0

    for i in range(1,n+1):
        for j in range(1,w+1):
            if j >= _cost[i-1]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-_cost[i-1]] + _benefit[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    benefit = dp[n][w]
    
    i = n
    j = w
    while i>0 and j>0:
        if dp[i][j] != dp[i-1][j]:
            solution.append(i-1)
            j = j-_cost[i-1]
            i = i-1
        else:
            i=i-1

    return benefit, weigth, solution[::-1]

print("#2")

for cost_limit in [9, 10, 20, 30, 40, 50, 60, 100, 150, 200, 1000]:
    sol = knapsack(benefits,costs,cost_limit)
    print('cost_constraint:' + str(cost_limit).rjust(5) + \
    ', b/c: ' + str(str(sol[0]) + '/' + str(sol[1])).rjust(7) + \
    ', solution: ' + str(sol[2]))

print("#3")
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

scrum_tasks.extend(scrum_tasks)

benefits = [task[1] for task in scrum_tasks]
costs =  [task[2] for task in scrum_tasks]

for cost_limit in [9, 10, 20, 30, 40, 50, 60, 100, 150, 200, 1000]:
    sol = knapsack(benefits,costs,cost_limit)
    print('cost_constraint:' + str(cost_limit).rjust(5) + \
    ', b/c: ' + str(str(sol[0]) + '/' + str(sol[1])).rjust(7) + \
    ', solution: ' + str(sol[2]))


sys.stdout = orig_stdout
f.close()