from lib import create_circular_queue, rotate_and_remove


"""
TODO:
- josephus_problem 구현하기
    # 요세푸스 문제 구현
        # 1. 큐 생성
        # 2. 큐가 빌 때까지 반복
        # 3. 제거 순서 리스트 반환
"""


def josephus_problem(n: int, k: int) -> list[int]:
    """
    1부터 n까지 원형 큐를 만들고, 매번 k번째 사람을 제거하여
    그 제거된 순서를 리스트에 담아 반환합니다.
    """
    q: deque[int] = create_circular_queue(n)
    result: list[int] = []

    # 큐가 빌 때까지 k번째 요소를 제거 후 기록
    while q:
        removed = rotate_and_remove(q, k)
        result.append(removed)

    return result

def solve_josephus() -> None:
    """입, 출력 format"""
    n: int
    k: int
    n, k = map(int, input().split())
    result: list[int] = josephus_problem(n, k)
    
    # 출력 형식: <3, 6, 2, 7, 5, 1, 4>
    print("<" + ", ".join(map(str, result)) + ">")

if __name__ == "__main__":
    solve_josephus()