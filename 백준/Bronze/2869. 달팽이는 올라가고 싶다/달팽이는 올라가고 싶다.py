am_height, sleep_height, height = map(int, input().split())

height -= sleep_height
my_height = am_height - sleep_height
day = height / my_height

if day - (height // my_height) != 0:
    day = (height // my_height) + 1

print(int(day))