from collections import deque


n, m = 4, 6
lst = [[1, 0, 1, 1, 1, 1], [1, 1, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 1]]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
is_success = False

start_x, start_y = 0, 0
end_x, end_y = n-1, m-1

# queue : 내가 갈 수 있는 길의 후보
queue = deque()
queue.append((start_x, start_y))

# visited : 내가 이미 간 곳들의 집합
vistied = set()
vistied.add((start_x, start_y))

for i in lst:
    print(i)
    
while queue:
    x, y = queue.popleft()
    print(x, y)
    if (x, y) == (end_x, end_y):
        is_success = True
        break

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]


        # 그리드 안에 있니?         갈 수 있는 길이니?      방문을 안했니?
        if (0<=nx<n and 0<=ny<m) and (lst[nx][ny] == 1) and ((nx, ny) not in vistied):
            # 큐에 집어 넣어
            queue.append((nx, ny))
            vistied.add((nx, ny))

        # # 그리드 안에 있니?
        # if 0<=nx<n and 0<=ny<m:
        #     # 갈 수 있는 길이니?
        #     if lst[nx][ny] == 1:
        #         # 방문을 안했니?
        #         if (nx, ny) not in vistied:
        #             # 큐에 집어 넣어

        # if 0>nx or n<=nx or 0>ny or m<=ny:
        #     continue
        # # 큐에 집어 넣어

if is_success:
    print('도착!')
else:
    print('실패')


