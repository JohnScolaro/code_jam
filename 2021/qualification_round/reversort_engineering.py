def sum_sequential(i):
    return i * ((i+1)/2)

def solve() -> str:
    l, complexity = [int(x) for x in input().split(' ')]
    if complexity < l - 1:
        return "IMPOSSIBLE"
    if complexity > sum_sequential(l) - 1:
        return "IMPOSSIBLE"

    a = []
    for i in range(l, 0, -1):
        if sum(a) + i > complexity - (i - 2):
            a.append(1)
        else:
            a.append(i)
    
    # number != 1 if we have to construct a large flip
    # else, we don't.
    b = list(range(1, l+1))
    for i in reversed(range(l)):
        if a[i] == 1:
            pass
        else:
            b = b[0:i] + b[i:][::-1]
    return ' '.join([str(x) for x in b])


T = int(input())
 
for t in range(1, T + 1):
    print ("Case #{}: {}".format(str(t), str(solve())))
