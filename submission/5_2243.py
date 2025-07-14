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


def main() -> None:
    """
    명령 형식:
      1 b   : 상자에서 누적 순서가 b번째인 사탕의 맛 번호를 찾아 출력하고, 해당 사탕을 1개 제거
      2 b c : 맛 번호 b인 사탕을 c개 추가(또는 제거, c는 음수일 수 있음)
    각 명령을 처리할 때마다 필요한 출력을 표준 출력으로 보냅니다.
    """
    input = sys.stdin.readline
    n = int(input().strip())
    MAX_FLAVOR = 1_000_000
    st = SegmentTree[int, int](MAX_FLAVOR)

    for _ in range(n):
        parts = list(map(int, input().split()))
        if parts[0] == 1:
            b = parts[1]
            flavor = st.find_by_order(b)
            st.update(flavor, -1)
            print(flavor)
        else:
            b, c = parts[1], parts[2]
            st.update(b, c)


if __name__ == "__main__":
    main()