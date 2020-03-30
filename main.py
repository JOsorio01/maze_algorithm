# Global maze maze
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [2, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 3],
    [1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


def find_position(matriz, numb):
    for y_index in range(len(matriz)):
        for x_index in range(len(matriz[y_index])):
            if matriz[y_index][x_index] == numb:
                return [x_index, y_index]


def difference(a, b):
    if len(a) == 2 and len(b) == 2:
        if a[0] == b[0] and a[1] == b[1]:
            return False
    return True


def check_position(x, y, start, prev):
    if x < 0 or y < 0:
        return 1
    else:
        return maze[y][x]


def get_walls(up, down, left, right):
    count = 0
    if up == 1:
        count += 1
    if down == 1:
        count += 1
    if left == 1:
        count += 1
    if right == 1:
        count += 1
    return count


def get_through(start, prev=[]):
    x = start[0]
    y = start[1]

    up = check_position(x, y - 1, start, prev)
    down = check_position(x, y + 1, start, prev)
    left = check_position(x - 1, y, start, prev)
    right = check_position(x + 1, y, start, prev)

    if up == 3 or down == 3 or left == 3 or right == 3:
        maze[y][x] = 2
        return maze
    else:
        if up == 0 and difference(prev, [x, y - 1]):
            maze[y][x] = 2
            return get_through([x, y - 1], start)
        elif down == 0 and difference(prev, [x, y + 1]):
            maze[y][x] = 2
            return get_through([x, y + 1], start)
        elif right == 0 and difference(prev, [x + 1, y]):
            maze[y][x] = 2
            return get_through([x + 1, y], start)
        elif left == 0 and difference(prev, [x - 1, y]):
            maze[y][x] = 2
            return get_through([x - 1, y], start)
        else:
            maze[y][x] = 1
            if up == 2:
                return get_through([x, y - 1], start)
            elif down == 2:
                return get_through([x, y + 1], start)
            elif right == 2:
                return get_through([x + 1, y], start)
            elif left == 2:
                return get_through([x - 1, y], start)


if __name__ == '__main__':
    start = find_position(maze, 2)
    solve = get_through(start)
    for row in solve:
        print(row)
