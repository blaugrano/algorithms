from typing import Callable

import pytest
from collections import deque


def dec_to_bin(n: int) -> int:
    out = deque()
    while n > 0:
        print(n)
        out.appendleft(n % 2)
        n //= 2
    return out


# print(dec_to_bin(5))

"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
ans[i] is the number of 1's in the binary representation of i.

O(n*log(n))
"""


def count_representations_bits(n: int) -> list[int]:
    counters = []
    for n in range(n + 1):
        counter = 0
        while n > 0:
            if n % 2:
                counter += 1
            n //= 2
        counters.append(counter)
    return counters


""""
DP approach
- We don't need to actually 'build' each representation, but remember the sum of the right part
- Total of 1's for n is the most significant bit plus the bits of 2**i behind (offset). This
  is the part of the representation that repeats

O(n)
"""


def count_representations_bits_dp(n: int) -> list[int]:
    dp = [0] * (n + 1)
    offset = 1
    for i in range(1, n + 1):
        if i == offset * 2:
            offset = i
        dp[i] = 1 + dp[i - offset]  # most significant bit + 2**i behind (offset)
    return dp


"""
ex.:

- for n = 5:
                              offset
idx   0     1     2     3     4     5
1's   0     1     1     2     1     2
      (000) (001) (010) (011) (100) (101)
              01 <----------------- 1 + _01
"""


@pytest.mark.parametrize("n,exp", [(2, [0, 1, 1]), (5, [0, 1, 1, 2, 1, 2])])
@pytest.mark.parametrize("count_representations_bits_func", [count_representations_bits, count_representations_bits_dp])
def test_hamming_weight(n: int, exp: int, count_representations_bits_func: Callable[[int], list[int]]):
    assert count_representations_bits_func(n) == exp
