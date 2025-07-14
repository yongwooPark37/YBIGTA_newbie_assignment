from lib import SegmentTree
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