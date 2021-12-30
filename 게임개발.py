#기본 입력
n,m = map(int,input().split())
x,y,dir = map(int,input().split())
game_map = list()
for _ in range(n):
    game_map.append(list(map(int,input().split())))


# 필요한 변수 생성
visited = [[0]*m for _ in range(n)]
visited[x][y] =1
step = [(-1,0),(0,1),(1,0),(0,-1)]

def turn_left():
    global dir
    dir -=1
    if dir < 0:
        dir = 3

turn_count = 0
count = 1
while True:
    turn_left()
    nx = x + step[dir][0]
    ny = y + step[dir][1]

    if (nx < 0 or ny < 0 or nx >= n or ny >= m or game_map[nx][ny] ==1 or visited[nx][ny] ==1):
        turn_count += 1
        if turn_count == 4:
            #3번 진행
            nx = x - step[dir][0]
            ny = y - step[dir][1]
            if game_map[nx][ny] == 1:
                break
            else:
                turn_count = 0
                x = nx
                y = ny
                continue
        else:
            continue
    else:
        turn_count = 0
        count += 1
        x = nx
        y = ny
        visited[x][y] = 1

print(count)
