import ConnectFourBrain
from ConnectFourBoard import *
import ConnectFourAI

board = ConnectFourBoard()

turn = 0
v=-1
while v==-1:
	
	if turn==0:
		print board
		col=ConnectFourAI.findSmartMove(board,0)
		#col=int(raw_input("Which column? "))
	else:
		print board
		col=ConnectFourAI.findSmartMove(board,1)
		print "playing " + str(col)

	board.move(col, turn)
	if turn==0: turn=1
	else: turn=0
	v=ConnectFourBrain.victory(board)

print board
print str(v) +" wins"