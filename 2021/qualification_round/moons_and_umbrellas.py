def solve() -> str:
    min_cost = 0
    x, y, art = input().split(' ')
    minimised_cost_art = ''.join([x for x in art if x != '?'])
    for i in range(len(minimised_cost_art) - 1):
        if minimised_cost_art[i:i+2] == 'CJ':
            min_cost += int(x)
        if minimised_cost_art[i:i+2] == 'JC':
            min_cost += int(y)
    return min_cost
 
T = int(input())
 
for t in range(1, T + 1):
    print ("Case #{}: {}".format(str(t), str(solve())))
