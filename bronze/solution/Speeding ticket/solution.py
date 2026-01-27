# 문제 요약
# Bessie is driving a car for 100km and she changes the speed in the middle sometimes.
# Ex) 0km~40km --> 65kmph, 40km~70km --> 40kmph, 70km~100km --> 80kmph
# A road that Bessie is riding a car on has speed limit. However, it is different for each part of the road
# Ex) 0km~30km --> speed limit: 70kmph, 30km~80kmph --> speed limit: 35kmph, 80km~100km --> speed limit: 60kmph
# We have to find maximum speed that Bessie's car's speed exceeds the speed limit. (answer: speed - speed limit)
# If Bessie has never exceeded the speed limit, print 0
N,M = list(map(int,input().split()))
N_list = []
M_list = []
cur_N = 0
cur_M = 0
for _ in range(N):
    N_len, N_spd = list(map(int,input().split()))
    cur_N += N_len
    N_list.extend([cur_N, N_spd])
for _ in range(M):
    M_len, M_spd = list(map(int,input().split()))
    cur_M += M_len
    M_list.extend([cur_M, M_spd])
N_idx = 0
M_idx = 0
ans = 0
while N_idx < N * 2 and M_idx < M * 2:
    if M_list[M_idx + 1] - N_list[N_idx + 1] > ans:
        ans = M_list[M_idx + 1] - N_list[N_idx + 1]
    if N_list[N_idx] < M_list[M_idx]:
        N_idx += 2
    elif N_list[N_idx] > M_list[M_idx]:
        M_idx += 2
    else:
        N_idx += 2
        M_idx += 2
print(ans)