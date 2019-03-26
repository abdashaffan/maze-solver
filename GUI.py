# Tugas Kecil IF2211 Strategi Algoritma
# Abda Shaffan D 13517021
# Juniardi Akbar 13517075

#import turtle as T  #kakas yang digunakan untuk menggambar maze

# wn = T.Screen()
# wn.bgcolor("black")
# wn.title("Maze Solver using BFS and A* algorithm")
# wn.setup(700, 700)

# class Pen(T.Turtle):
#     def __init__(self):
#         self.shape("square")
#         self.color("white")
#         self.penup()
#         self.speed(0)


def main():
    # Parse maze data from text file
    with open("maze-sm.txt", "r") as f:
        data = f.readlines()

    matrix = []
    for line in data:
        newLine = []
        for letter in line:
            if (letter != '\n'):
                newLine.append(int(letter))
        matrix.append(newLine)
    print(matrix)


if __name__ == "__main__":
    main()