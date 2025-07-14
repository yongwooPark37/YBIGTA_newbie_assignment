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