for i in range(int(input())):
    n, m = map(int, input().split())
    print(max(0, n - m) + n)