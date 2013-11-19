from ConnectFourBrain import *
from ConnectFourBoard import *
import random

def move(board):
	col=random.randint(0,board.rows())
	while board.height(col)>=board.cols():
		col=random.randInt(0,board.rows())

	return col