import itertools

def divisibleSumPairs(n, k, ar):
    # Write your code here
    pair = 0
    comb = list(itertools.combinations(ar, 2))
    for i in comb:
        if sum(i) % k == 0:
            pair += 1

    print(pair)


divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2])