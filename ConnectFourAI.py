from ConnectFourBrain import *
from ConnectFourBoard import *
import random

def findRandomMove(board):
	moves=ConnectFourBrain.validMoves()
	i=random.randint(0,len(moves))
	return moves[i]
	
def findSmartMove(board):
	return

def minimax(board, player, depth, maximizingPlayer):
	if ConnectFourBrain.victory(board):
		
	if depth=0:
		return heuristic(board)
	
	moves=ConnectFourBrain.validMoves(board)
	
	if maximizingPlayer:
		bestValue=-1000
		for m in moves:
			
	

def heuristic(board):
	return 0