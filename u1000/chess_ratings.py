for i in range(int(input())):
    x, y = map(int, input().split())
    print(ceil((y - x) / 8))