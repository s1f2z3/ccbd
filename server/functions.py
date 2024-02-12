def definchetian(st1:str, st2:str, pr =True):
    m = len(st1) + 1
    n = len(st2) + 1
    # Using nested loops to create a 2D list (table)
    #table = [[i for i in range(m)] for _ in range(n)]


    table = []
    for i in range(n):
        t = []
        for j in range(m):
            if i == 0:
                t.append(j)
            elif j == 0:
                t.append(i)
            else:
                t.append(0)
        table.append(t)

    for i in range(n):
        for j in range(m):
            if i == 0:
                break
            elif j == 0:
                continue
            else:
                a = table[i-1][j] + 1
                b = table[i][j-1] + 1
                c = table[i-1][j-1] 
                if st1[j-1] != st2[i-1]:
                    c += 1
                table[i][j] = min( a, b, c)

    # Display the table
    if pr:
        for row in table:
            print(row)

    return table[n-1][m-1]





if __name__ == '__main__':
    a = definchetian('islam','ilsam')
    print(a)