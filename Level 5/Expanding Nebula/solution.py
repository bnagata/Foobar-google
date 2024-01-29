from collections import defaultdict

def generate(r,s,cols):
    a = r & ~(1<<cols)
    c = r >> 1
    b = s & ~(1<<cols)
    d = s >> 1
    return (a&~b&~c&~d) | (~a&b&~c&~d) | (~a&~b&c&~d) | (~a&~b&~c&d)

def build_map(cols, nums):
    mapping = defaultdict(set)
    nums = set(nums)
    for r in range(1<<(cols+1)):
        for s in range(1<<(cols+1)):
            generation = generate(r,s,cols)
            if generation in nums:
                mapping[(generation, r)].add(s)
    return mapping

def solution(grid):
    grid = list(zip(*grid))
    cols = len(grid[0])

    nums = [sum([1<<r if col else 0 for r, col in enumerate(row)]) for row in grid]
    mapping = build_map(cols, nums)

    preimage = {r: 1 for r in range(1<<(cols+1))}
    for row in nums:
        next_row = defaultdict(int)
        for c1 in preimage:
            for c2 in mapping[(row, c1)]:
                next_row[c2] += preimage[c1]
        preimage = next_row
    result = sum(preimage.values())

    return result

if __name__ in '__main__':
    grid = [[True, True, False, True, False, True, False, True, True, False],
                   [True, True, False, False, False, False, True, True, True, False],
                   [True, True, False, False, False, False, False, False, False, True],
                   [False, True, False, False, False, False, True, True, False, False]]
    result = solution(grid)
    print(result)