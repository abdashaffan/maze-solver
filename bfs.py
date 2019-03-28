import queue as queue


def CekTetangga(start, arrived, matriks):
    brs = len(matriks)
    kol = len(matriks[0])
    b = start[0]
    k = start[1]
    count = 0
    if (b - 1 >= 0):
        if (matriks[b - 1][k] == 0 and not (arrived[b - 1][k])):
            count = count + 1
    if (b + 1 < brs):
        if (matriks[b + 1][k] == 0 and not (arrived[b + 1][k])):
            count = count + 1
    if (k - 1 >= 0):
        if (matriks[b][k - 1] == 0 and not (arrived[b][k - 1])):
            count = count + 1
    if (k + 1 < kol):
        if (matriks[b][k + 1] == 0 and not (arrived[b][k + 1])):
            count = count + 1
    return count


def getTetangga(start, arrived, matriks):
    brs = len(matriks)
    kol = len(matriks[0])
    b = start[0]
    k = start[1]
    res = []
    if (b - 1 >= 0):
        if (matriks[b - 1][k] == 0 and not (arrived[b - 1][k])):
            res.append([(b - 1), k])
    if (b + 1 < brs):
        if (matriks[b + 1][k] == 0 and not (arrived[b + 1][k])):
            res.append([(b + 1), k])
    if (k - 1 >= 0):
        if (matriks[b][k - 1] == 0 and not (arrived[b][k - 1])):
            res.append([b, (k - 1)])
    if (k + 1 < kol):
        if (matriks[b][k + 1] == 0 and not (arrived[b][k + 1])):
            res.append([b, (k + 1)])

    return res


def isTetangga(A, B):
    if (A[0] == B[0]):
        if (A[1] == B[1] - 1):
            return True
        elif (A[1] == B[1] + 1):
            return True
        else:
            return False
    elif (A[1] == B[1]):
        if (A[0] == B[0] - 1):
            return True
        elif (A[0] == B[0] + 1):
            return True
        else:
            return False
    else:
        return False


def BFS(q, akhir, arrived, solusi, maze):
    brs = len(maze)
    kol = len(maze[0])
    matriks = []
    for i in range(brs):
        M = []
        for j in range(kol):
            M.append(int(maze[i][j]))
        matriks.append(M)
    start = q.get()
    arrived[start[0]][start[1]] = True
    tetangga = CekTetangga(start, arrived, matriks)
    jalur = [start]

    while (tetangga == 1):
        next = getTetangga(start, arrived, matriks)[0]
        tetangga = CekTetangga(next, arrived, matriks)
        start = next
        arrived[start[0]][start[1]] = True
        jalur.append(start)

    if (start == akhir):
        solusi.append(jalur)
        return True
    else:
        if (tetangga == 0):
            return False
        else:
            for i in getTetangga(start, arrived, matriks):
                q.put(i)
            solusi.append(jalur)
            return False


def getBFSPath(start, finish, maze):
    arrived = []
    for i in range(len(maze)):
        arr = []
        for j in range(len(maze[0])):
            arr.append(False)
        arrived.append(arr)

    q = queue.Queue()
    q.put(start)
    found = False
    solusi = []
    while (not (q.empty()) and not (found)):
        found = BFS(q, finish, arrived, solusi, maze)

    res = [solusi[0]]
    solusi.pop(0)

    while (len(res) > 0):
        path = res.pop(0)

        node = path[-1]
        if (node == finish):
            break

        for i in solusi:
            if (isTetangga(node, i[0])):
                new_path = list(path)
                for j in i:
                    new_path.append(j)
                res.append(new_path)
    return path