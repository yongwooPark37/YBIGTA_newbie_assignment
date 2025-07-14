from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional, Iterable


"""
TODO:
- Trie.push 구현하기
- (필요할 경우) Trie에 추가 method 구현하기
"""


T = TypeVar("T")


@dataclass
class TrieNode(Generic[T]):
    body: Optional[T] = None
    children: list[int] = field(default_factory=lambda: [])
    is_end: bool = False


class Trie(list[TrieNode[T]]):
    def __init__(self) -> None:
        super().__init__()
        self.append(TrieNode(body=None))

    def push(self, seq: Iterable[T]) -> None:
        """
        seq: T의 열 (list[int]일 수도 있고 str일 수도 있고 등등...)

        action: trie에 seq을 저장하기
        """
        node = 0
        for c in seq:
            if not hasattr(self[node], "_children_map"):
                m: dict[T, int] = {}
                for ch_idx in self[node].children:
                    b = self[ch_idx].body
                    assert b is not None
                    m[b] = ch_idx
                setattr(self[node], "_children_map", m)

            cmap: dict[T, int] = getattr(self[node], "_children_map")
            nxt = cmap.get(c)
            if nxt is None:
                # 3) 새 노드 추가
                new_idx = len(self)
                self.append(TrieNode(body=c))
                self[node].children.append(new_idx)
                cmap[c] = new_idx
                nxt = new_idx

            node = nxt
        # 마지막 글자 노드에 is_end 표시
        self[node].is_end = True


import sys


"""
TODO:
- 일단 lib.py의 Trie Class부터 구현하기
- main 구현하기

힌트: 한 글자짜리 자료에도 그냥 str을 쓰기에는 메모리가 아깝다...
"""


def main() -> None:
    """
    1. N개의 이름을 입력받아 Trie에 삽입
    2. 각 노드별로 자식 서브트리를 블록으로 보고 순열 계산 (DFS)
    3. 팩토리얼 곱하기
    4. 결과를 1,000,000,007로 나눈 값을 출력
    """
    input = sys.stdin.readline
    MOD = 1_000_000_007

    # 1) 입력 및 Trie 구축
    n = int(input().strip())
    trie: Trie[str] = Trie()
    for _ in range(n):
        word = input().rstrip()
        trie.push(word)

    # 2) 팩토리얼 미리 계산
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % MOD

    # 3) DFS로 서브트리별 경우의 수 계산
    def dfs(node_idx: int) -> int:
        total = 1
        for c in trie[node_idx].children:
            total = total * dfs(c) % MOD
        k = len(trie[node_idx].children)
        total = total * fact[k] % MOD
        return total

    # 4) 루트(0번)에서 시작해서 전체 경우의 수 출력
    print(dfs(0))


if __name__ == "__main__":
    main()