"""
Fibonacci
OR
Climbing stairs: DP bottom-up for how many ways to climb n steps with 1 or 2 steps
    #################################
    # step           #  0 1 2 3 4 5 #
    #################################
    # possibilities  #  8 5 3 2 1 1 #
    # from last step #  <---------| #
    #################################
"""


def climb_stairs(n: int) -> int:
    a, b = 1, 1
    for _ in range(n - 1):
        b = a + b
        a = b - a
    return b


# print(climb_stairs(5))


"""
Unique Paths (matrix)

? R _ _ _ _ 1     ^
D _ _ _ _ _ 1     |
1 1 1 1 1 1 1   <-|
n x m

1. Start calculating penultimate row (row) according to bottom row (p_row)
2. Keep moving up and building the entire row but skipping last elem (1) when calculating x = a + b:
    _____
    |x a|
    |b  |
    -----
"""


def unique_paths(m: int, n: int) -> int:
    p_row = [1] * n  # remember last row
    for y in range(m - 1):  # or (n - 2, -1, -1) bottom-up, but y is not used anyway
        row = [1] * n
        for x in range(n - 2, -1, -1):  # right-left, skipping right-most (1)
            row[x] = row[x + 1] + p_row[x]
        p_row = row
    return p_row[0]  # return from p_row, which at this point is already 'row'


print(unique_paths(1, 2))
print(unique_paths(2, 2))
print(unique_paths(7, 3))
print(unique_paths(13, 11))
