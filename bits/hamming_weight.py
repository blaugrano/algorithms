from typing import Callable
import pytest


def hamming_eight_naive(n: int) -> int:
    counter = 0
    for b in bin(n)[2:]:
        if b == '1':
            counter += 1
    return counter


def hamming_weight(n: int) -> int:
    total = 0
    while n:
        total += n % 2
        n = n >> 1
    return total


def hamming_weight_and(n: int) -> int:
    total = 0
    while n:
        n &= (n - 1)
        total += 1
    return total


@pytest.mark.parametrize("n,expected", [(0, 0), (1, 1), (5, 2), (10, 2), (2, 1), (4294967293, 31)])
@pytest.mark.parametrize("hamming_weight_func", [hamming_eight_naive, hamming_weight, hamming_weight_and])
def test_hamming_weight(n: int, expected: int, hamming_weight_func: Callable[[int], int]):
    assert hamming_weight_func(n) == expected