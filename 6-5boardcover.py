def set(box, y, x, type, delta):
    result = True
    for i in range(3):
        ny = y + covertype[type][i][0]
        nx = x + covertype[type][i][1]
        if ny < 0 or ny >= len(box) or nx < 0 or nx >= len(box[0]):
            result = False
        else:
            box[ny][nx] += delta
            if box[ny][nx] > 1:
                result = False
    return result


def cover(box):
    y = -1
    x = -1
    for i in range(len(box)):
        for j in range(len(box[i])):
            if box[i][j] == 0:
                y = i
                x = j
                break
        if y != -1:
            break
    if y == -1:
        return 1
    ret = 0
    for type in range(4):
        if set(box, y, x, type, 1):
            ret += cover(box)
        set(box, y, x, type, -1)
    return ret


if __name__ == "__main__":
    covertype = [[[0, 0], [1, 0], [0, 1]],
                 [[0, 0], [0, 1], [1, 1]],
                 [[0, 0], [1, 0], [1, 1]],
                 [[0, 0], [1, 0], [1, -1]]]

    game_n = int(input())
    for _ in range(game_n):
        line, row = map(int, input().split())
        box = [[1 for _ in range(row)] for _ in range(line)]

        white = 0
        for i in range(line):
            Tiles = list(input())
            for j in range(row):
                if Tiles[j] == '.':
                    box[i][j] = 0
                    white += 1
        if white % 3 != 0:
            print(0)
        else:
            print(cover(box))
