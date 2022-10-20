import sys

input = sys.stdin.readline

def dfs(r, c, idx, total):
    global ans
    if ans >= total + max_val * (3 - idx):
        return # 현재 가능한 최대값보다 큰 값일 경우 return (최적화를 위한 가지치기)
    if idx == 3:
        ans = max(ans, total)
        return
    else:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0:
                if idx == 1: # ㅜ 모양을 위해 한 블럭 2번 탐색하게 하기
                    visit[nr][nc] = 1
                    dfs(r, c, idx + 1, total + arr[nr][nc])
                    visit[nr][nc] = 0
                visit[nr][nc] = 1
                dfs(nr, nc, idx + 1, total + arr[nr][nc])
                visit[nr][nc] = 0


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

visit = [([0] * M) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

ans = 0

max_val = max(map(max, arr))

for r in range(N):
    for c in range(M):
        visit[r][c] = 1
        dfs(r, c, 0, arr[r][c])
        visit[r][c] = 0

print(ans)
