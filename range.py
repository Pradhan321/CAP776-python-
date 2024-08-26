n = int(input())
m = int(input())

for n in range(n, m + 1):
    if (n > 1):
        i = 2
        f = False
        while (d*d<=n):
            if (n % i == 0):
                f = True
                break
            i += 1
        if (f == False):
            print(n,end=' ')
