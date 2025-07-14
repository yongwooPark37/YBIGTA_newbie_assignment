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