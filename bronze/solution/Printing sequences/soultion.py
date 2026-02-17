def solve1(l):
    if len(l) == 0: # l이 비었다는 뜻
        return True
    return min(l) == max(l) # l 안의 수가 전부 같은 값이라는 뜻

def solve2(l):
    if solve1(l):   # 만약 solve1의 조건에 걸렸었다면
        return True
    r = 0
    blocks = []
    while r < len(l):   # r은 l의 길이보다 작을 동안 1씩 늘어남
        i = r
        while r < len(l) and l[r] == l[i]:  # l에서 같은 숫자가 반복되는 동안 loop
            r += 1
        blocks.append((r - i, l[i]))    # l에서 어떤 숫자가 몇 번 반복해서 나오는지 확인하고 blocks에 append
    return len(blocks) % 2 == 0 and blocks[2:] == blocks[:-2]   # blocks의 길이가 짝수고 blocks 안의 tuple들이 반복되는지 확인

def solve3(l):
    for i in range(1, len(l) + 1):
        if len(l) % i == 0: # 만약 l의 길이가 i로 정확하게 나누어진다면
            if l[:-len(l) // i] == l[len(l) // i:]: # l 안의 숫자들이 반복되는지 확인
                substring = l[:len(l) // i] # 반복되는 숫자 substring 확인
                for i in range(len(substring) + 1): # substring 안에서도 숫자가 반복되는지 확인
                    if solve2(substring[:i]) and solve1(substring[i:]):
                        return True
                    if solve1(substring[:i]) and solve2(substring[i:]):
                        return True
def solve():
    N, K = map(int, input().split())
    seq = list(map(int, input().split()))
    if K == 1:
        return solve1(seq)  # K의 값이 1일 때는 solve1 사용
    elif K == 2:
        return solve2(seq)  # K의 값이 2일 때는 solve2 사용
    else:
        assert K == 3
        return solve3(seq)  # K의 값이 3일 때는 solve3 사용

T = int(input())
for _ in range(T):
    print("YES" if solve() else "NO")   # 결과에 따라서 "YES" 또는 "NO" print