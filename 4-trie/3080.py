from lib import Trie
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