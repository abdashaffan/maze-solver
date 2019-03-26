# Tugas Kecil 3 IF2211 Strategi Algoritma
# Abda Shaffan D 13517021
# Juniardi Akbar 13517075


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

# Resize ukuran block pada maze jika ukuran maze terlalu besar


def blockSize(numOfRows):
    # if numOfRows > 40:
    #     return 15
    # elif numOfRows > 30:
    #     return 20
    return 24  # default pen size


# Fungsi pembuat maze
def init_maze(maze, windowHeight, windowWidth, blockSize):

    pen = Pen()

    for y in range(len(maze)):
        for x in range(len(maze[y])):

            block = maze[y][x]

            # Setting supaya mazenya ada di tengah window
            scr_x = -windowWidth/2 + x*blockSize + 0.5*blockSize
            scr_y = windowHeight/2 - y*blockSize - 0.5*blockSize

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
    print('Masukkan nama file tempat maze disimpan (dengan .txt)')
    print('(harus ada di dalam folder mazes) : ', end='')
    fileName = input()

    print('Masukkan koordinat titik start <x y>: ', end='')
    xStart, yStart = map(int, input().split())
    print('Masukkan koordinat titik finish <x y>: ', end='')
    xFinish, yFinish = map(int, input().split())

    print("Kok ga dianggep :(")  # Di-ignore sampe windownya di-close

    # Menyimpan data matrix dari text file di dalam folder "mazes"
    # Hanya bisa menerima bentuk maze persegi panjang (sisi yang berhadapan panjangnya sama)

    with open(os.path.join("./mazes", fileName), "r") as f:
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

    # Set titik start dan finish
    temp1 = list(maze[xStart])
    temp1[yStart] = 'S'
    maze[xStart] = ''.join(temp1)

    temp2 = list(maze[xFinish])
    temp2[yFinish] = 'F'
    maze[xFinish] = ''.join(temp2)

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
    init_maze(maze, windowHeight, windowWidth, BLOCK_SIZE)

    wn.exitonclick()
    # turtle.done()


# Memanggil program utama
if __name__ == "__main__":
    main()
