n, scores = int(input()), input().split()
print(sorted(set(list(map(int, scores))))[-2])