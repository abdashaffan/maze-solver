
import turtle
import os
from bfs import *
import queue

'''
BAGIAN PENGATURAN GUI
'''
BG_COLOR = 'black'
PEN_COLOR = 'white'
BLOCK_SIZE = 24

# Kelas dari modul turtle yang dipakai untuk menggambar maze
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.hideturtle()
        self.penup()
        self.shape("square")
        self.color(PEN_COLOR)
        self.speed(0)


class Cell():
    def __init__(self, point, parentPoint, symbol):
        self.point = Point(point.x, point.y)
        self.parentPoint = Point(parentPoint.x, parentPoint.y)
        self.isWall = (symbol == '0')


# Fungsi pembuat maze
def initMaze(maze, windowHeight, windowWidth, startPoint, finishPoint):

    pen = Pen()

    for x in range(len(maze)):
        for y in range(len(maze[0])):
            p = [x,y]
            block = maze[x][y]

            # Setting supaya mazenya ada di tengah window
            setPosition(pen, p, windowHeight, windowWidth)

            if (x == startPoint.x and y == startPoint.y):
                pen.color('red')
                pen.stamp()
            elif (x == finishPoint.x and y == finishPoint.y):
                pen.color('blue')
                pen.stamp()
            elif block == '1':
                pen.color(PEN_COLOR)
                pen.stamp()


# Asumsi: pada maze hanya terdapat 1 entrace dan 1 exit
def setEntraceExit(maze, startPoint, finishPoint):
    row = len(maze)
    col = len(maze[0])
    p1 = []
    p2 = []
    for i in range(col):
        if (maze[0][i] == '0'):
            p1.extend([0, i])
        if (maze[row - 1][i] == '0'):
            p2.extend([(row - 1), i])

    for i in range(row):
        if (maze[i][0] == '0'):
            if not p1:
                p1.extend([i, 0])
            elif not p2:
                p2.extend([i, 0])
        if (maze[i][col - 1] == '0'):
            if not p1:
                p1.extend([i, (col - 1)])
            elif not p2:
                p2.extend([i, (col - 1)])

    print("(1) <" + str(p1[0]) + "," + str(p1[1]) + ">")
    print("(2) <" + str(p2[0]) + "," + str(p2[1]) + ">")
    print('pilih posisi start (1/2): ')
    choice = input()
    if choice == '1':
        xStart = p1[0]
        yStart = p1[1]
        xFinish = p2[0]
        yFinish = p2[1]
    elif choice == '2':
        xStart = p2[0]
        yStart = p2[1]
        xFinish = p1[0]
        yFinish = p1[1]

    # pass startPoint and finishPoint
    startPoint.x = xStart
    startPoint.y = yStart
    finishPoint.x = xFinish
    finishPoint.y = yFinish

    return maze

#Set posisi pen pada posisi window tempat penggambaran akan dilakukan
def setPosition(pen, point, winHeight, winWidth):

    scr_x = -winWidth/2 + point[1]*BLOCK_SIZE + 0.5*BLOCK_SIZE
    scr_y = winHeight/2 - point[0]*BLOCK_SIZE - 0.5*BLOCK_SIZE

    pen.goto(scr_x, scr_y)

#Menggambar 1 petak path pada turtle
def drawPath(pen, point, winHeight, winWidth):
    pen.color('green')
    setPosition(pen, point, winHeight, winWidth)
    pen.stamp()

#Menghapus 1 petak path pada turtle
def erasePath(pen, point, winHeight, winWidth):
    pen.color(BG_COLOR)
    setPosition(pen, point[0], point[1], winHeight, winWidth)
    pen.stamp()


def animatePath(path, winHeight, winWidth):
    pen = Pen()
    for point in path:
        drawPath(pen, point, winHeight, winWidth)


'''
BAGIAN ALGORITMA PENYELESAIAN
'''
def manhattanDistance(p1, p2):
    return (abs(p1.x-p2.x) + abs(p1.y-p2.y))


'''
PROGRAM UTAMA
'''
def main():

    # Input nama file
    print('Nama file(tanpa tambahan .txt)')
    print('(harus ada di dalam folder mazes) : ', end='')
    fileName = input()

    # Menyimpan data matrix dari text file di dalam folder "mazes"
    # Hanya bisa menerima bentuk maze persegi panjang (sisi yang berhadapan panjangnya sama)
    with open(os.path.join("./mazes", fileName + ".txt"), "r") as f:
        data = f.readlines()

    # Import data ke array 2D
    maze = []
    for row in data:
        # Hapus newline jika ada
        if (row[-1] == '\n'):
            mazeRow = row[:-1]
        else:
            mazeRow = row
        maze.append(mazeRow)

    startPoint = Point()
    finishPoint = Point()

    maze = setEntraceExit(maze, startPoint, finishPoint).copy()

    start = [startPoint.x, startPoint.y]
    finish = [finishPoint.x, finishPoint.y]


    ############### BIKIN 1 FUNGSI SENDIRI DI bfs.py ###############
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
    while (not(q.empty()) and not(found)):
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

    #mengembalikan path hasil pencarian, akan digunakan pada animasi
    ############### BIKIN 1 FUNGSI SENDIRI DI bfs.py ###############
    
    #Set ukuran window
    windowHeight = len(maze)*BLOCK_SIZE
    windowWidth = len(maze[0])*BLOCK_SIZE

    # Set window GUI
    wn = turtle.Screen()
    wn.bgcolor(BG_COLOR)
    if (len(maze) <= 25 and len(maze[0]) <= 25):
        wn.setup(height=1.0, width=1.0)
    else:
        wn.screensize(windowHeight, windowWidth)
    wn.title("Maze solver dengan BFS dan A*")

    # Membuat maze
    initMaze(maze, windowHeight, windowWidth, startPoint, finishPoint)
    #Menggambar path final pada GUI
    animatePath(path,windowHeight,windowWidth)

    wn.exitonclick()
    # turtle.done()


# Memanggil program utama
if __name__ == "__main__":
    main()
