from lib import Trie
import sys


"""
TODO:
- 일단 Trie부터 구현하기
- count 구현하기
- main 구현하기
"""


def count(trie: Trie[str], query_seq: str) -> int:
    """
    trie - 이름 그대로 trie
    query_seq - 단어 ("hello", "goodbye", "structures" 등)

    returns: query_seq의 단어를 입력하기 위해 버튼을 눌러야 하는 횟수
    """
    pointer = 0
    cnt = 1

    for element in query_seq:
        if cnt > 1:  
            if len(trie[pointer].children) > 1 or trie[pointer].is_end:
                cnt += 1
        
        new_index: int = 0
        for child_idx in trie[pointer].children:
            if trie[child_idx].body == element:
                new_index = child_idx
                break
        pointer = new_index

    return cnt


def main() -> None:
    """
    여러 테스트 케이스를 읽어서 각 케이스마다 단어들을 입력하기 위한
    버튼 누름 횟수의 평균(소수 둘째 자리까지)을 한 줄에 하나씩 출력합니다.
    """
    input = sys.stdin.readline
    output_lines: list[str] = []

    while True:
        line = input()
        if not line:
            break
        if not line.strip():
            continue
        n = int(line.strip())
        trie: Trie[str] = Trie()
        # 사전 단어 삽입
        for _ in range(n):
            word = input().strip()
            trie.push(word)

        # 질의 개수
        q = int(input().strip())
        total_presses = 0
        for _ in range(q):
            query = input().strip()
            total_presses += count(trie, query)

        avg = total_presses / q
        output_lines.append(f"{avg:.2f}")

    sys.stdout.write("\n".join(output_lines))


if __name__ == "__main__":
    main()