linked = [
    ['xxx.............'],
    ['...x...x.x.x....'],
    ['....x.....x...xx'],
    ['x...xxxx........'],
    ['......xxx.x.x...'],
    ['x.x...........xx'],
    ['...x..........xx'],
    ['....xx.x......xx'],
    ['.xxxxx..........'],
    ['...xxx...x...x..'],
]

if __name__ == "__main__":
    game_n = int(input())
    for _ in range(game_n):
        clocks = list(map(lambda x: int(int(x)/3) - 1, input().split()))
        print(clocks)