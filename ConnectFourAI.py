from ConnectFourBrain import *
from ConnectFourBoard import *
import random
import copy
import ConnectFourBrain

def findRandomMove(board):
	moves=ConnectFourBrain.validMoves(board)
	i=random.randint(0,len(moves)-1)
	return moves[i]

#5 returns an answer in a ~3 seconds
def findSmartMove(board, playerOptimizingFor):
	ignore, moves = minimax(board,playerOptimizingFor,playerOptimizingFor,5)
	print ignore
	print moves
	i=random.randint(0,len(moves)-1)
	return moves[i]

def minimax(board, playerOptimizingFor, playerTurn, depth):
	maxstep=playerOptimizingFor==playerTurn
	winningPlayer = ConnectFourBrain.victory(board)
	if winningPlayer!=-1:
		if winningPlayer==playerOptimizingFor: return 1000+depth, []
		else: return -1000-depth, []
		
	if depth<=0:
		return heuristic(board, playerOptimizingFor), []

	moves=ConnectFourBrain.validMoves(board)
	
	if maxstep:
		bestValue=-10000
		bestMoves=[]
		for m in moves:
			newBoard=copy.deepcopy(board)
			newBoard.move(m,playerTurn)
			val, ignore = minimax(newBoard, playerOptimizingFor,
				(playerTurn+1) % 2, depth-1)
			if val>bestValue:
				bestMoves=[m]
				bestValue=val
			elif val==bestValue:
				bestMoves.append(m)
				bestValue=val
	else:
		bestValue=10000
		bestMoves=[]
		for m in moves:
			newBoard=copy.deepcopy(board)
			newBoard.move(m,playerTurn)
			val, ignore = minimax(newBoard, playerOptimizingFor,
				(playerTurn+1) % 2, depth-1)
			if val<bestValue:
				bestMoves=[m]
				bestValue=val
			elif val==bestValue:
				bestMoves.append(m)
				bestValue=val
	
	return bestValue, bestMoves


def heuristic(board, playerOptimizingFor):
	return 0