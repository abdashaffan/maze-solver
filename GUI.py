# Tugas Kecil IF2211 Strategi Algoritma
# Abda Shaffan D 13517021
# Juniardi Akbar 13517075


#Program utama
def main():

    #Menyimpan data matrix dari text file
    with open("maze-sm.txt", "r") as f:
        data = f.readlines()

    matrix = []

    for row in data:
        #di akhir text harus ada newline
        matrixRow = row[:-1]
        matrix.append(matrixRow)
    print(matrix)


if __name__ == "__main__":
    main()