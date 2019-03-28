from copy import *


class Block(object):
    # ctor
    def __init__(self, x, y, symbol):
        # Koordinat posisi blok pada maze
        self.x = x
        self.y = y
        self.parent = None  # block
        self.isAWall = (symbol == '1')
        self.F = 0
        self.G = 0
        self.H = 0

    # method
    def setAdjacentG(self, adj):
        adj.G = self.G + 1

    def setAdjacentH(self, finish, adj):
        # Menerima adjacent block, YANG DIRUBAH BUKAN SELFNYA
        # Heuristik: Manhattan Distance
        adj.H = (abs(adj.y - finish.y) + abs(adj.x - finish.x))

    def setAdjacentF(self, adj):
        adj.F = adj.G + adj.H

    def setAdjacentParent(self, adj):
        adj.parent = self

    # input adalah block yang bertetangga dengan current, dan yang akan diupdate
    def Update(self, adj, finish):
        newG = self.G + 1
        if (newG < adj.G or adj.G == 0):
            self.setAdjacentG(adj)
            self.setAdjacentH(finish, adj)
            self.setAdjacentF(adj)
            self.setAdjacentParent(adj)


class mazeSolver(object):
    def __init__(self, maze, start, finish):
        # Maze berupa array 2D
        self.maze = maze.copy()
        self.opened = []
        self.closed = []
        self.blockList = []
        self.start = Block(start[0], start[1], maze[start[0]][start[1]])
        self.finish = Block(finish[0], finish[1], maze[finish[0]][finish[1]])

    def initBlocks(self):
        # dipanggil didalam method A* inti
        # start dan finish berupa list [x,y]
        row = len(self.maze)
        col = len(self.maze[0])
        for i in range(row):
            for j in range(col):
                self.blockList.append(Block(i, j, self.maze[i][j]))

    def getBlock(self, x, y):
        # x dan y adalah koordinat maze yang VALID
        for block in self.blockList:
            if (block.x == x and block.y == y):
                return block

    def isBlockExist(self, x, y):
        for block in self.blockList:
            if (block.x == x and block.y == y):
                return True
        return False

    def searchLowestF(self):
        # Mencari block dengan F value yang paling rendah
        minFCostBlock = 100000000
        minBlock = None
        for block in self.opened:
            if (block.F < minFCostBlock):
                minFCostBlock = block.F
                minBlock = block

        return minBlock

    def moveBlock(self, minFBlock):
        # memindahkan block current dari opened ke closed list
        for i in range(len(self.opened)):
            if (self.opened[i].x == minFBlock.x
                    and self.opened[i].y == minFBlock.y):
                self.closed.append(self.opened.pop(i))
                break

    def getAdjacentBLock(self, currentBlock):
        # Mengembalikan list of Block yang berisi semua tetangga dari currentBlock
        adjacentList = []
        adjDxDy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for d in adjDxDy:
            if self.isBlockExist(currentBlock.x + d[0], currentBlock.y + d[1]):
                adjacentList.append(
                    self.getBlock(currentBlock.x + d[0],
                                  currentBlock.y + d[1]))

        return adjacentList

    def isInClosed(self, block):
        for b in self.closed:
            if (b.x == block.x and b.y == block.y):
                return True
            return False

    # Hanya untuk debug
    def printPath(self, currentBlock):
        print("Backtrack jalur yang ditemukan: ")
        block = currentBlock
        while (block.x != self.start.x or block.y != self.start.y):
            print("(" + str(block.x) + "," + str(block.y) + ")")
            block = block.parent

    def generateSolution(self, currentBlock):
        solution = []
        block = currentBlock
        while (block.x != self.start.x or block.y != self.start.y):
            point = [block.x, block.y]
            solution.append(point)
            block = block.parent
        point = [self.start.x, self.start.y]
        solution.append(point)
        solution.reverse()
        return solution

    # Method utama pada kelas, mengembalikan list of point sebagai path solusi
    def solveAStar(self):
        self.initBlocks()
        self.opened.append(self.start)
        while (len(self.opened) > 0):
            currentBlock = self.searchLowestF()
            # Transfer currentBlock dari opened ke closed list
            self.moveBlock(currentBlock)

            # basis
            if (currentBlock.x == self.finish.x
                    and currentBlock.y == self.finish.y):
                return self.generateSolution(currentBlock)

            # rekurens
            adjacentList = self.getAdjacentBLock(currentBlock)
            for nBlock in adjacentList:
                if (nBlock in self.closed or nBlock.isAWall):
                    continue
                else:
                    currentBlock.Update(nBlock, self.finish)

                    if nBlock not in self.opened:
                        self.opened.append(nBlock)

        if (len(self.opened <= 0)):
            return []
