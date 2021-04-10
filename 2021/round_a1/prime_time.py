"""
This answer didn't quite get the solution to the question.
Given 30 more miinutes I think I could have gotten more than just the first
test case.

I have a small bug somewhere in the 'generating possible products' part of the
code. Lines 34 -> 41.

I think I solved the rest of the question efficiently though. This code jam was
a lot of fun.
"""

def pduct(a):
    if len(a) == 1:
        return a[0]
    else:
        i = 1
        for x in range(len(a)):
            i *= a[x]
        return i

import itertools

def solve() -> str:
    M = int(input())
    
    cards = []
    for _ in range(M):
        P, N = [int(e) for e in input().split()]
        for z in range(N):
            cards.append(P)

    # Get the max possible sum
    max_sum = sum(cards[1:])
    # Get all possible products
    all_prods = set()
    for i in range(len(cards)):
        for x in itertools.permutations(cards, i):
            a = pduct(list(x))
            if a < max_sum:
                all_prods.add(a)

    print(all_prods)
    
    valid_prods = []

    # For each product, get lowest factors, and remove them from a copy of cards.
    for prod in all_prods:
        fresh_cards = cards.copy()
        p = prod
        
        while p > 1:
            for i in range(len(fresh_cards)):
                if p % fresh_cards[i] == 0:
                    p /= fresh_cards[i]
                    fresh_cards.pop(i)
                    break
        

        if sum(fresh_cards) == prod:
            valid_prods.append(prod)

    print(valid_prods)
    if valid_prods == []:
        return 0
    else:
        return max(valid_prods)

 
T = int(input())
 
for t in range(1, T + 1):
    print ("Case #{}: {}".format(str(t), solve()))
