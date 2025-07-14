from lib import SegmentTree
import sys


"""
TODO:
- 일단 SegmentTree부터 구현하기
- main 구현하기
"""


def main() -> None:
    """
      1) 초기 DVD 개수 n, 요청 개수 m 입력
      2) 초기에는 DVD i가 위치 m+i (1-based) 에 쌓여 있음
      3) 요청 순서대로 DVD x를 꺼낼 때마다:
         a. DVD x 위에 있는 DVD 개수를 계산하여 출력합니다.
         b. 꺼낸 DVD를 맨 위(현재 top 위치)로 이동시킵니다.
    """
    input = sys.stdin.readline
    t = int(input().strip())

    for _ in range(t):
        n, m = map(int, input().split())
        # 전체 크기: n + m (최대 위치)
        size = n + m + 1
        st = SegmentTree[int, int](size)

        # 현재 DVD i 의 위치 (1-based)
        pos = [0] * (n + 1)
        # 초기 위치: m+1 .. m+n
        for i in range(1, n + 1):
            pos[i] = m + i
            st.update(pos[i], 1)

        top = m  # 앞으로 꺼낼 때마다 이 위에 쌓을 것

        def range_sum(l: int, r: int) -> int:
            """
            세그먼트 트리에서 [l..r] 구간의 합을 구합니다.
            """
            res = 0
            l = l - 1 + st.n
            r = r - 1 + st.n
            while l <= r:
                if l & 1:
                    res += st.tree[l]
                    l += 1
                if not (r & 1):
                    res += st.tree[r]
                    r -= 1
                l //= 2
                r //= 2
            return res

        qs = list(map(int, input().split()))
        out = []
        for x in qs:
            if pos[x] > 1:
                above = range_sum(1, pos[x] - 1)
            else:
                above = 0
            out.append(str(above))

            # 꺼낸 뒤 맨 위로 이동
            st.update(pos[x], -1)
            st.update(top, 1)
            pos[x] = top
            top -= 1

        sys.stdout.write(" ".join(out) + "\n")


if __name__ == "__main__":
    main()