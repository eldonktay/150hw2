from __future__ import print_function
import copy, random
MOVES = {0:'up', 1:'left', 2:'down', 3:'right'}
#tracks the highest tile
Htile = 2

class State:
	"""game state information"""
	#Hint: probably need the tile matrix, which player's turn, score, previous move
	def __init__(self, matrix, player, score, pre_move):
		matrix = []
		
	def highest_tile(self):
		"""Return the highest tile here (just a suggestion, you don't have to)"""
		return Htile

class Gametree:
	"""main class for the AI"""
	#Hint: Two operations are important. Grow a game tree, and then compute minimax score. 
	#Hint: To grow a tree, you need to simulate the game one step. 
	#Hint: Think about the difference between your move and the computer's move. 
	def __init__(self, root, depth):
		pass
	def grow_once(self, state):
		"""Grow the tree one level deeper"""
		pass
	def grow(self, state, height):
		"""Grow the full tree from root"""
		pass
	def minimax(self, state):
		"""Compute minimax values on the three"""
		pass
	def compute_decision(self):
		"""Derive a decision"""
		#Replace the following decision with what you compute
		decision = random.randint(0,3)
		#Should also print the minimax value at the root
		print(MOVES[decision])
		return decision

class Simulator:
	"""Simulation of the game"""
	#Hint: You basically need to copy all the code from the game engine itself.
	#Hint: The GUI code from the game engine should be removed. 
	#Hint: Be very careful not to mess with the real game states. 
	def __init__(self, matrix, score):
		pass
	def move(self, direction):
		#whenever I move in x direction, I need to place blocks, update the score, and match together
		if(1)
		
		if(2)
		
		if(3)
		
		if(4)
	def moveTiles(self):
		pass
	def mergeTiles(self):
		#the tile in the direction that gets merged will merge, then the score will double and add to the score
		pass
	def checkIfCanGo(self):
		pass
	def canMove(self):
		pass
	def rotateMatrixClockwise(self):	
		pass		
	def convertToLinearMatrix(self):
		pass
