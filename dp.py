def climb_stairs(n: int) -> int:
    """
    Fibonacci
    OR
    DP bottom-up for how many ways to climb n steps with 1 or 2 steps
        #################################
        # step           #  0 1 2 3 4 5 #
        #################################
        # possibilities  #  8 5 3 2 1 1 #
        # from last step #  <---------| #
        #################################
    """
    a, b = 1, 1
    for _ in range(n - 1):
        b = a + b
        a = b - a
    return b


print(climb_stairs(5))
