import sys


def move():
    global K, robot_position

    new_robot_position = []
    for i in robot_position:
        idx = i
        next_idx = (idx + 1) % distance
        if robot_lst[next_idx][0] == 0 and durability[next_idx] > 0:
            if next_idx == down_station:
                robot_lst[idx] = [0]
            else:
                robot_lst[idx], robot_lst[next_idx] = [0], (robot_lst[idx][0], next_idx)
                new_robot_position.append(next_idx)

            durability[next_idx] -= 1
            if durability[next_idx] == 0:
                K -= 1
        else:
            new_robot_position.append(idx)

    robot_position = new_robot_position


def put_up(x):
    global K

    if durability[x] > 0 and robot_lst[x][0] == 0:
        robot_position.append(x)
        robot_lst[x] = (cnt, x)

        durability[x] -= 1
        if durability[x] == 0:
            K -= 1


N, K = map(int, sys.stdin.readline().split())
durability = list(map(int, sys.stdin.readline().split()))
distance = 2 * N

robot_lst = [[0] for _ in range(distance)]
cnt = 0
up_station = 0
down_station = N - 1
robot_position = []
while K > 0:
    cnt += 1

    up_station = (up_station - 1) % distance
    down_station = (down_station - 1) % distance
    if robot_lst[down_station][0]:
        robot_lst[down_station] = [0]
        robot_position.remove(down_station)

    move()
    put_up(up_station)

print(cnt)

