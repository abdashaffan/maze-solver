
import turtle
import os


BG_COLOR = 'black'
BLOCK_SIZE = 24


# Kelas dari modul turtle yang dipakai untuk menggambar maze
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("square")
        self.color("white")
        self.speed(0)

# Asumsi: pada maze hanya terdapat 1 entrace dan 1 exit


def setEntraceExit(maze):
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

    print("(1) <" + str(p1[0]) + " , " + str(p1[1]) + ">")
    print("(2) <" + str(p2[0]) + " , " + str(p2[1]) + ">")
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

    # Set titik start dan finish
    temp1 = list(maze[xStart])
    temp1[yStart] = 'S'
    maze[xStart] = ''.join(temp1)

    temp2 = list(maze[xFinish])
    temp2[yFinish] = 'F'
    maze[xFinish] = ''.join(temp2)

    return maze


# Fungsi pembuat maze


def init_maze(maze, windowHeight, windowWidth):

    pen = Pen()

    for y in range(len(maze)):
        for x in range(len(maze[y])):

            block = maze[y][x]

            # Setting supaya mazenya ada di tengah window
            scr_x = -windowWidth/2 + x*BLOCK_SIZE + 0.5*BLOCK_SIZE
            scr_y = windowHeight/2 - y*BLOCK_SIZE - 0.5*BLOCK_SIZE

            # Gambar tembok
            pen.goto(scr_x, scr_y)
            if block == 'S':
                pen.color('red')
                pen.stamp()
            elif block == 'F':
                pen.color('green')
                pen.stamp()
            elif block == '1':
                pen.color('white')
                pen.stamp()


# Program utama
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

    maze = setEntraceExit(maze).copy()

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
    init_maze(maze, windowHeight, windowWidth)

    wn.exitonclick()


# Memanggil program utama
if __name__ == "__main__":
    main()
