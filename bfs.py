import queue as queue
from colored import fg, bg, attr

def CekTetangga(start, arrived):
    global matriks, brs, kol
    b = start[0]
    k = start[1]
    count = 0
    if (b-1 >= 0):
        if (matriks[b-1][k] == 0 and not(arrived[b-1][k])):
            count = count+1
    if (b+1 < brs):
        if (matriks[b+1][k] == 0 and not(arrived[b+1][k])):
            count = count+1
    if (k-1 >= 0):
        if (matriks[b][k-1] == 0 and not(arrived[b][k-1])):
            count = count+1
    if (k+1 < kol):
        if (matriks[b][k+1] == 0 and not(arrived[b][k+1])):
            count = count+1
    return count

def getTetangga(start, arrived):
    global matriks, brs, kol
    b = start[0]
    k = start[1]
    res = []
    if (b-1 >= 0):
        if (matriks[b-1][k] == 0 and not(arrived[b-1][k])):
            res.append([(b-1),k])
    if (b+1 < brs):
        if (matriks[b+1][k] == 0 and not(arrived[b+1][k])):
            res.append([(b+1),k])
    if (k-1 >= 0):
        if (matriks[b][k-1] == 0 and not(arrived[b][k-1])):
            res.append([b,(k-1)])
    if (k+1 < kol):
        if (matriks[b][k+1] == 0 and not(arrived[b][k+1])):
            res.append([b,(k+1)])
    
    return res

def isTetangga(A, B):
    if (A[0] == B[0]):
        if (A[1] == B[1]-1):
            return True
        elif (A[1] == B[1]+1):
            return True
        else:
            return False
    elif (A[1] == B[1]):
        if (A[0] == B[0]-1):
            return True
        elif (A[0] == B[0]+1):
            return True
        else:
            return False
    else:
        return False
    

def BFS(q,akhir,arrived,solusi):
    global matriks, brs, kol
    start = q.get()
    arrived[start[0]][start[1]] = True
    tetangga = CekTetangga(start, arrived)
    jalur = [start]

    while (tetangga == 1):
        next = getTetangga(start, arrived)[0]
        tetangga = CekTetangga(next, arrived)
        start = next
        arrived[start[0]][start[1]] = True
        jalur.append(start)
    
    if (start == akhir):
        solusi.append(jalur)
        return True
    else:
        if (tetangga == 0):
            # solusi.append(jalur)
            return False
        else:
            for i in getTetangga(start, arrived):
                q.put(i)
            solusi.append(jalur)
            return False

# MAIN PROGRAM

text = input()
text = text.split()

brs = int(text[0])
kol = int(text[1])
matriks = []
arrived = []
for i in range(brs):
    m = []
    arr = []
    text = input()
    for j in range(kol):
        arr.append(False)
        el = int(text[j])
        m.append(el)
    arrived.append(arr)
    matriks.append(m)

text = input()
text = text.split()
awal = [int(text[0]), int(text[1])]

text = input()
text = text.split()
akhir = [int(text[0]), int(text[1])]

q = queue.Queue()
q.put(awal)
found = False
solusi = []
while (not(q.empty()) and not(found)):
    found = BFS(q,akhir,arrived,solusi)

idx = 0
res = [solusi[0]]
solusi.pop(0)

# print(res)
# print(solusi)

while (len(res)>0):
    path = res.pop(0)
    
    node = path[-1]
    # print(path)
    if (node == akhir):
        break

    for i in solusi:
        if (isTetangga(node, i[0])):
            new_path = list(path)
            for j in i:
                new_path.append(j)
            res.append(new_path)

print(path)
# for i in range(brs):
#     for j in range(kol):
#         temp = [i,j]
#         if (temp in path):
#             print('%s%s%d%s' % (fg(16),bg(5),matriks[i][j],attr(0)) ,end="")
#         else:
#             print(matriks[i][j], end="")
#     print()