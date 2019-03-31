import queue as queue

def getChild(start, arrived, matriks):
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

def BFS(start, finish, maze):
    # Proses inisialisasi pembentukan matriks maze dan arrived
    brs = len(maze)
    kol = len(maze[0])
    matriks = []
    arrived = []
    for i in range(brs):
        M = []
        arr = []
        for j in range(kol):
            M.append(int(maze[i][j]))
            arr.append(False)
        
        matriks.append(M)
        arrived.append(arr)
    
    # Panggil fungsi getBFSPath untuk dapat jalur
    return getBFSPath(start,finish,arrived,matriks)

def getBFSPath(start, finish, arrived, matriks):
    queue = []
    queue.append([start])
    while queue:
        path = queue.pop(0)
        node = path[-1]
        arrived[node[0]][node[1]] = True
        
        #Jika sudah selesai return jalur
        if (node == finish):
            return path

        # Menambahkan antrian setiap node anaknya
        for n in getChild(node, arrived, matriks):
            temp = list(path)
            temp.append(n)
            queue.append(temp)
            # Isi queue adalah jalur-jalur yang telah dilewati
