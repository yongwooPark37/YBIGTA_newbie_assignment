# lib.py의 Matrix 클래스를 참조하지 않음
import sys


"""
TODO:
- fast_power 구현하기 
"""


def fast_power(base: int, exp: int, mod: int) -> int:
    """
    빠른 거듭제곱 알고리즘 구현
    분할 정복을 이용하여 log 시간에 계산 가능
    """
    result = 1
    base %= mod

    while exp > 0:
        if exp & 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp >>= 1

    return result

def main() -> None:
    A: int
    B: int
    C: int
    A, B, C = map(int, input().split()) # 입력 고정
    
    result: int = fast_power(A, B, C) # 출력 형식
    print(result) 

if __name__ == "__main__":
    main()
