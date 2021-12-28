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
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-_cost[i-1]] + _benefit[i-1]):
            else:
                dp[i][j] = dp[i-1][j]
    benefit = dp[n][w]

    return benefit, weigth, solution
'''
if ( dp[i-1][j-_cost[i-1]]+_benefit[i-1] > dp[i-1][j]):
                    dp[i][j] = dp[i-1][j-_cost[i-1]]+_benefit[i-1]
                    if(dp[i][j] > dp[i][j-1]):
                        solution.append(i)
                        weigth += _cost[i-1]
'''

knapsack(benefits,costs,200)

