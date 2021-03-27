def solve() -> str:
    n = int(input())
    l = [int(x) for x in input().split(' ')]
    
    complexity = 0
    for i in range(n - 1):
        j = l.index(min(l[i:]))
        complexity += j - i + 1
        l = l[:i] + l[i:j+1][::-1] + l[j+1:]    
    return complexity
 
T = int(input())
 
for t in range(1, T + 1):
    print ("Case #{}: {}".format(str(t), str(solve())))
