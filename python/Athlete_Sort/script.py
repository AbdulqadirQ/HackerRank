if __name__ == '__main__':
    nm = input().split(" ")

    n,m = int(nm[0]), int(nm[1])

    rows = []
    for athletes in range(n):
        rows.append(list(map(int, input().rstrip().split(" "))))

    k = int(input())

    rows.sort(key=lambda x: x[k])

    for row in rows:
        print(' '.join(map(str, row)))
