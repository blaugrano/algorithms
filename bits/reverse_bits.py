from typing import Callable

import pytest


# Reverse bits of a given 32 bits unsigned integer.

def reverse_bits_(n: int) -> int:
    reader = 1
    new_n = 0
    writer = 2147483648  # 1000...0
    for _ in range(32):
        if n & reader:
            new_n |= writer
        reader <<= 1
        writer >>= 1
    return new_n


def reverse_bits(n: int) -> int:
    res = 0
    for i in range(32):
        bit = (n >> i) & 1
        res |= (bit << (31 - i))
    return res


@pytest.mark.parametrize("n,exp", [(0, 0),
                                   (3310900316, 975837859),
                                   (43261596, 964176192),
                                   (4294967293, 3221225471),
                                   (4294967295, 4294967295)])
@pytest.mark.parametrize("reverse_bits_func", [reverse_bits, reverse_bits_])
def test_hamming_weight(n: int, exp: int, reverse_bits_func: Callable[[int], int]):
    assert reverse_bits_func(n) == exp
