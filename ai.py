from __future__ import print_function
import copy, random
MOVES = {0:'up', 1:'left', 2:'down', 3:'right'}
#tracks the highest tile
Htile = 2

class State:
    """game state information"""
    #Hint: probably need the tile matrix, which player's turn, score, previous move
    def __init__(self, matrix, player, score, pre_move):
        self.matrix = matrix
        self.player = player
        self.score = score
        self.pre_move = pre_move
        
        
    def highest_tile(self):
        """Return the highest tile here (just a suggestion, you don't have to)"""
        return Htile

class Gametree:
    """main class for the AI"""
    #Hint: Two operations are important. Grow a game tree, and then compute minimax score.
    #Hint: To grow a tree, you need to simulate the game one step.
    #Hint: Think about the difference between your move and the computer's move.
    def __init__(self, root, depth):
        self.root = root
        self.depth = depth
        
    def grow_once(self, state):
        direc = []
        #create a simulator for 4 possible moves
        simulator0 = Simulator(state, matrix, state.score)
        simulator1 = Simulator(state, matrix, state.score)
        simulator2 = Simulator(state, matrix, state.score)
        simulator3 = Simulator(state, matrix, state.score)
        
        #move in all 4 directions
        simulator0.move(state, 0)
        simulator1.move(state, 1)
        simulator2.move(state, 2)
        simulator3.move(state, 3)
        
        #direc[0] = new State(self, simulator0.tileMatrix, state.player, simulator0.total_points, state)
        #direc[1] = new State(self, simulator1.tileMatrix, state.player, simulator1.total_points, state)
        #direc[2] = new State(self, simulator2.tileMatrix, state.player, simulator2.total_points, state)
        #direc[3] = new State(self, simulator3.tileMatrix, state.player, simulator3.total_points, state)
        
        #get the biggest score
        n = 0
        for i in direc:
            if direc[i] > n:
                n = direc[i].score
        return direc, n
    
    #grow function    
    def grow(self, state, height):
        """Grow the full tree from root"""
        tree = []
        n = 0
        if height == 1:
            tree, n = grow_once(self, state)
            return tree, n
            
        
    def minimax(self, state):
        """Compute minimax values on the three"""
        pass
    def compute_decision(self):
        """Derive a decision"""
        #depth = 1 is max
        if self.depth == 1:
            decision = grow_once(self, state)
        #depth = 2 is random    
        if self.depth == 2:
            decision = random.randint(0,3)
        #depth = 3 is max-min-max
        if self.depth == 3:
            decision = grow(self, state, height)
        #Should also print the minimax value at the root
        print(MOVES[decision])
        return decision

class Simulator:
    """Simulation of the game"""
    #Hint: You basically need to copy all the code from the game engine itself.
    #Hint: The GUI code from the game engine should be removed.
    #Hint: Be very careful not to mess with the real game states.
    def __init__(self, matrix, score):
        self.total_points = 0
        self.default_tile = 2
        self.board_size = 4
        pygame.init()
        #self.surface = pygame.display.set_mode((400, 500), 0, 32)
        #pygame.display.set_caption("2048")
        #self.myfont = pygame.font.SysFont("arial", 40)
        #self.scorefont = pygame.font.SysFont("arial", 30)
        self.tileMatrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.undoMat = []
        
    def move(self, direction):
        self.addToUndo()
        for i in range(0, direction):
            self.rotateMatrixClockwise()
        if self.canMove():
            self.moveTiles()
            self.mergeTiles()
            self.placeRandomTile()
        for j in range(0, (4 - direction) % 4):
            self.rotateMatrixClockwise()
        #self.printMatrix()
        
    def moveTiles(self):
        tm = self.tileMatrix
        for i in range(0, self.board_size):
            for j in range(0, self.board_size - 1):
                while tm[i][j] == 0 and sum(tm[i][j:]) > 0:
                    for k in range(j, self.board_size - 1):
                        tm[i][k] = tm[i][k + 1]
                    tm[i][self.board_size - 1] = 0
                    
    def mergeTiles(self):
        #the tile in the direction that gets merged will merge, then the score will double and add to the score
        tm = self.tileMatrix
        for i in range(0, self.board_size):
            for k in range(0, self.board_size - 1):
                if tm[i][k] == tm[i][k + 1] and tm[i][k] != 0:
                    tm[i][k] = tm[i][k] * 2
                    #logic for the highest tile, if the merged tile is higher than the current high then it will update
                    if tm[i][k] > Htile:
                        Htile = tm[i][k]
                    tm[i][k + 1] = 0
                    self.total_points += tm[i][k]
                    self.moveTiles()
                    
    def checkIfCanGo(self):
        tm = self.tileMatrix
        for i in range(0, self.board_size ** 2):
            if tm[int(i / self.board_size)][i % self.board_size] == 0:
                return True
        for i in range(0, self.board_size):
            for j in range(0, self.board_size - 1):
                if tm[i][j] == tm[i][j + 1]:
                    return True
                elif tm[j][i] == tm[j + 1][i]:
                    return True
        return False
        
    def canMove(self):
        tm = self.tileMatrix
        for i in range(0, self.board_size):
            for j in range(1, self.board_size):
                if tm[i][j-1] == 0 and tm[i][j] > 0:
                    return True
                elif (tm[i][j-1] == tm[i][j]) and tm[i][j-1] != 0:
                    return True
        return False
        
    def rotateMatrixClockwise(self):
        tm = self.tileMatrix
        for i in range(0, int(self.board_size/2)):
            for k in range(i, self.board_size- i - 1):
                temp1 = tm[i][k]
                temp2 = tm[self.board_size - 1 - k][i]
                temp3 = tm[self.board_size - 1 - i][self.board_size - 1 - k]
                temp4 = tm[k][self.board_size - 1 - i]
                tm[self.board_size - 1 - k][i] = temp1
                tm[self.board_size - 1 - i][self.board_size - 1 - k] = temp2
                tm[k][self.board_size - 1 - i] = temp3
                tm[i][k] = temp4
                
    def convertToLinearMatrix(self):
        m = []
        for i in range(0, self.board_size ** 2):
            m.append(self.tileMatrix[int(i / self.board_size)][i % self.board_size])
        m.append(self.total_points)
        return m
