
sum = [0,0,0,0]

for i in range(2,51,2):
    if i % 3 == 0 and i % 5 == 0:
        print('Three and Five')
        sum[3] = sum[3] + 1
    elif i % 3 == 0:
        print('Three')
        sum[1] = sum[1] + 1
    elif i % 5 == 0:
        print('Five')
        sum[2] = sum[2] + 1
    else:
        print(i)

    sum[0] = sum[0] + i

print("\n","Total:",sum[0],",Three:",sum[1],",Five:",sum[2],",Three and Five:",sum[3])