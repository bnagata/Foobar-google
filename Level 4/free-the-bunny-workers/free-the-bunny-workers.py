from itertools import combinations


def solution(num_buns, num_required):
    c = list(combinations(range(num_buns), num_buns - num_required + 1))
    return [
        [key for key, bunnies in enumerate(c) if bunny in bunnies]
        for bunny in range(num_buns)
    ]
if __name__ in '__main__':
    result = solution(5,3)
    print(result)