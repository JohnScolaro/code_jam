"""
Solves the 'append sort' question from Google Code Jam 2021 Round A1.

It is a general solution, and efficient enough to get all the points for the
question.

This question was really fun to solve. It was roughly 15 minutes before I
thought I had completed the question, but actually took about 1.5 hours to
solve.

A useful test case to have would have been
100 1 1 1 1 1 1 1 1 1 1
which becomes:
100 101 102 103 104 105 106 107 108 109 110
and not:
100 101 102 103 104 105 106 107 108 109 1000
"""

def solve() -> str:
    N = input()
    
    line = input()
    line = [int(x) for x in line.split()]
    cnt = 0
    
    for i in range(len(line) - 1):
        num_chars_added = 0
        max_n = line[i+1]
        while (max_n <= line[i]):
            num_chars_added += 1
            max_n *= 10
            max_n += 9
        
        if (num_chars_added == 0):
            continue

        maximum_number = max_n
        minimum_number = line[i+1] * (10**num_chars_added)

        if line[i] < minimum_number:
            line[i+1] = minimum_number
            cnt += num_chars_added
        elif minimum_number <= line[i] < maximum_number:
            line[i+1] = line[i] + 1
            cnt += num_chars_added
        else:
            line[i+1] = maximum_number + 1
            cnt += num_chars_added + 1

    return cnt

 
T = int(input())
 
for t in range(1, T + 1):
    print ("Case #{}: {}".format(str(t), solve()))
