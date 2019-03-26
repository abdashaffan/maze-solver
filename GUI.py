# Tugas Kecil 3 IF2211 Strategi Algoritma
# Abda Shaffan D 13517021
# Juniardi Akbar 13517075


import turtle
import os


BG_COLOR = 'black'


# Definisi kelas dari modul turtle yang dipakai untuk menggambar pada GUI
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("square")
        self.color("white")
        self.speed(0)

# Resize ukuran block pada maze jika ukuran maze terlalu besar


def blockSize(numOfRows):
    if numOfRows > 40:
        return 15
    elif numOfRows > 30:
        return 20

    return 24  # default


# Fungsi pembuat maze
def init_maze(maze, pen, windowHeight, windowWidth, blockSize):
    for y in range(len(maze)):
        for x in range(len(maze[y])):

            block = maze[y][x]

            # Setting supaya mazenya ada di tengah window
            scr_x = -windowWidth/2 + x*blockSize + 0.5*blockSize
            scr_y = windowHeight/2 - y*blockSize - 0.5*blockSize

            # Gambar tembok
            if block == '1':
                pen.goto(scr_x, scr_y)
                pen.stamp()


# Program utama
def main():

    # Menyimpan data matrix dari text file di dalam folder "mazes"
    # Hanya bisa menerima bentuk maze persegi panjang (sisi yang berhadapan panjangnya sama)
    with open(os.path.join("./mazes", "maze-md.txt"), "r") as f:
        data = f.readlines()

    # Import data ke array 2D
    maze = []
    for row in data:
        if (row[-1] == '\n'):
            mazeRow = row[:-1]
        else:
            mazeRow = row
        maze.append(mazeRow)

    BLOCK_SIZE = blockSize(len(maze))

    windowHeight = len(maze)*BLOCK_SIZE
    windowWidth = len(maze[0])*BLOCK_SIZE

    # Setting window GUI
    wn = turtle.Screen()
    wn.bgcolor(BG_COLOR)
    # wn.screensize(windowHeight, windowWidth)
    wn.setup(height=1.0, width=1.0)
    wn.title("Maze solver dengan BFS dan A*")

    # Membuat maze
    pen = Pen()
    init_maze(maze, pen, windowHeight, windowWidth, BLOCK_SIZE)

    turtle.done()


# Memanggil program utama
if __name__ == "__main__":
    main()
