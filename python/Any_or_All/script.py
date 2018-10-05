n, inp_list = int(input()), input().split()

if all(list(map(lambda x: int(x)>0, inp_list))):
    print(any(list(map(lambda x: x == x[::-1], inp_list))))
else:
    print(False)