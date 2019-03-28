import turtle
import os
from bfs import *
from AStar import *
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


# Fungsi pembuat maze
def initMaze(maze, windowHeight, windowWidth, startPoint, finishPoint):

    pen = Pen()

    for x in range(len(maze)):
        for y in range(len(maze[0])):
            p = [x, y]
            block = maze[x][y]

            # Setting supaya mazenya ada di tengah window
            setPosition(pen, p, windowHeight, windowWidth)

            if (x == startPoint[0] and y == startPoint[1]):
                pen.color('red')
                pen.stamp()
            elif (x == finishPoint[0] and y == finishPoint[1]):
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
    startPoint.extend([xStart, yStart])
    finishPoint.extend([xFinish, yFinish])

    return maze


# Set posisi pen pada posisi window tempat penggambaran akan dilakukan


def setPosition(pen, point, winHeight, winWidth):

    scr_x = -winWidth / 2 + point[1] * BLOCK_SIZE + 0.5 * BLOCK_SIZE
    scr_y = winHeight / 2 - point[0] * BLOCK_SIZE - 0.5 * BLOCK_SIZE

    pen.goto(scr_x, scr_y)


# Menggambar 1 petak path pada turtle


def drawPath(pen, point, winHeight, winWidth, mode):
    if mode == 1:  # BFS
        pen.color('green')
    elif mode == 2:  # ASTAR
        pen.color('blue')
    setPosition(pen, point, winHeight, winWidth)
    pen.stamp()


# Menghapus 1 petak path pada turtle


def erasePath(pen, point, winHeight, winWidth):
    pen.color(BG_COLOR)
    setPosition(pen, point[0], point[1], winHeight, winWidth)
    pen.stamp()


def animatePath(path, winHeight, winWidth, mode):
    pen = Pen()
    for point in path:
        drawPath(pen, point, winHeight, winWidth, mode)


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

    start = []
    finish = []

    maze = setEntraceExit(maze, start, finish).copy()

    # mengembalikan path hasil pencarian, akan digunakan pada animasi
    # BFS
    pathBFS = getBFSPath(start, finish, maze)
    # AStar, sebelumnya membuat kelas solver terlebih dahulu
    AStar = mazeSolver(maze, start, finish)
    pathASTAR = AStar.solveAStar()

    # Set ukuran window
    windowHeight = len(maze) * BLOCK_SIZE
    windowWidth = len(maze[0]) * BLOCK_SIZE
    # Set window GUI
    wn = turtle.Screen()
    wn.bgcolor(BG_COLOR)
    if (len(maze) <= 25 and len(maze[0]) <= 25):
        wn.setup(height=1.0, width=1.0)
    else:
        wn.screensize(windowHeight, windowWidth)
    wn.title("Maze solver dengan BFS dan A*")

    # Membuat maze
    initMaze(maze, windowHeight, windowWidth, start, finish)

    # Menggambar path final pada GUI
    animatePath(pathBFS, windowHeight, windowWidth, 1)  # 1 = mode BFS
    animatePath(pathASTAR, windowHeight, windowWidth, 2)  # 2 = mode ASTAR

    wn.exitonclick()  # Menutup window maze jika diklik


# Memanggil program utama
if __name__ == "__main__":
    main()
