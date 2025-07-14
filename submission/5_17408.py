from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional, Callable


"""
TODO:
- SegmentTree 구현하기
"""


T = TypeVar("T")
U = TypeVar("U")


class SegmentTree(Generic[T, U]):
    def __init__(self, size: int) -> None:
        # 내부적으로 1-indexed complete binary tree 사용
        self.n = 1
        while self.n < size:
            self.n <<= 1
        # 트리 배열: 합 저장
        self.tree: list[int] = [0] * (2 * self.n)

    def update(self, idx: int, diff: int) -> None:
        """
        idx 위치(1-based)에 diff만큼 값을 더합니다.
        """
        pos = idx - 1 + self.n
        self.tree[pos] += diff
        pos //= 2
        while pos:
            self.tree[pos] = self.tree[2*pos] + self.tree[2*pos + 1]
            pos //= 2

    def find_by_order(self, k: int) -> int:
        """
        누적합으로 k번째 사탕(=prefix sum ≥ k)이 나오는 인덱스를 반환합니다.
        """
        idx = 1
        while idx < self.n:
            if self.tree[2*idx] >= k:
                idx = 2*idx
            else:
                k -= self.tree[2*idx]
                idx = 2*idx + 1

        return idx - self.n + 1


import sys


"""
TODO:
- 일단 SegmentTree부터 구현하기
- main 구현하기
"""


class Pair(tuple[int, int]):
    """
    힌트: 2243, 3653에서 int에 대한 세그먼트 트리를 만들었다면 여기서는 Pair에 대한 세그먼트 트리를 만들 수 있을지도...?
    """
    def __new__(cls, a: int, b: int) -> 'Pair':
        return super().__new__(cls, (a, b))

    @staticmethod
    def default() -> 'Pair':
        """
        기본값
        이게 왜 필요할까...?
        """
        return Pair(0, 0)

    @staticmethod
    def f_conv(w: int) -> 'Pair':
        """
        원본 수열의 값을 대응되는 Pair 값으로 변환하는 연산
        이게 왜 필요할까...?
        """
        return Pair(w, 0)

    @staticmethod
    def f_merge(a: Pair, b: Pair) -> 'Pair':
        """
        두 Pair를 하나의 Pair로 합치는 연산
        이게 왜 필요할까...?
        """
        return Pair(*sorted([*a, *b], reverse=True)[:2])

    def sum(self) -> int:
        return self[0] + self[1]


def main() -> None:
    # 구현하세요!
    pass


if __name__ == "__main__":
    main()