from __future__ import annotations
from collections import deque


"""
TODO:
- rotate_and_remove 구현하기 
"""


def create_circular_queue(n: int) -> deque[int]:
    """1부터 n까지의 숫자로 deque를 생성합니다."""
    return deque(range(1, n + 1))

def rotate_and_remove(queue: deque[int], k: int) -> int:
    """
    큐에서 k번째 원소를 제거하고 반환합니다.
    앞에서 (k-1)개를 뒤로 보내고 맨 앞(k번째)을 popleft로 제거합니다.
    """
    queue.rotate(-(k - 1))
    return queue.popleft()




"""
TODO:
- simulate_card_game 구현하기
    # 카드 게임 시뮬레이션 구현
        # 1. 큐 생성
        # 2. 카드가 1장 남을 때까지 반복
        # 3. 마지막 남은 카드 반환
"""


def simulate_card_game(n: int) -> int:
    """
    카드2 문제의 시뮬레이션
    맨 위 카드를 버리고, 그 다음 카드를 맨 아래로 이동
    """
    q: deque[int] = create_circular_queue(n)

    # 카드가 1장 남을 때까지
    while len(q) > 1:
        # 1) 맨 앞 카드 버리기
        rotate_and_remove(q, 1)
        # 2) 다음 카드를 꺼내서 맨 뒤로 붙이기
        card = rotate_and_remove(q, 1)
        q.append(card)

    return q[0]

def solve_card2() -> None:
    """입, 출력 format"""
    n: int = int(input())
    result: int = simulate_card_game(n)
    print(result)

if __name__ == "__main__":
    solve_card2()