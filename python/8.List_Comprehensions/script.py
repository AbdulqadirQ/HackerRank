x, y, z, n = [int(input()) for _ in range(4)]
print([[x_co,y_co,z_co] for x_co in range(x+1) for y_co in range(y+1) for z_co in range(z+1) \
    if sum([x_co, y_co, z_co]) is not n])