n = 4
def pascals_triangle(n):
    for i in range(1,n + 1):
        m = 1;
        for j in range(1,i + 1):
            print(m, end = " ")
            m = int(m * (i - j) / j)
        print("")

pascals_triangle(n)
