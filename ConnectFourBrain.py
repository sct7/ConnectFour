import ConnectFourBoard

def validMoves(board):
	moves=[]
	for col in range(board.cols()):
		if board.height(col)<board.rows(): moves.append(col)
	return moves

#returns -1 if no victor yet, 0 if player 0 has won, and 1 if player 1 has won
def victory(board):

	v=checkHoriz(board)
	if v!=-1:
		#print "h"
		return v

	v=checkVertical(board)
	if v!=-1:
		#print "v"
		return v

	v=checkUpDiag(board)
	if v!=-1:
		#print "ud"
		return v

	v=checkDownDiag(board)
	if v!=-1:
		#print "dd"
		return v	

	return -1

def checkHoriz(board):
	#print "checking h"
	for r in range(board.rows()):
		for c in range(board.cols()-3):
			#print "hh"
			#print c,r
			s=board.pos(c,r)
			if s!=-1 and [s]*4==board.section(c,r,4,1,0): return s
	return -1

def checkVertical(board):
	#print "checking v"
	for c in range(board.cols()):
		for r in range(board.rows()-3):
			#print "vv"
			#print c,r
			s=board.pos(c,r)
			if s!=-1 and [s]*4==board.section(c,r,4,0,1): return s
	return -1

def checkUpDiag(board):
	#print "checking ud"
	for c in range(board.cols()-3):
		for r in range(board.rows()-3):
			s=board.pos(c,r)
			if s!=-1 and [s]*4==board.section(c,r,4,1,1): return s
	return -1
def checkDownDiag(board):
	#print "checking dd"
	for c in range(board.cols()-3):
		for r in range(board.rows()-1,2,-1):
			s=board.pos(c,r)
			if s!=-1 and [s]*4==board.section(c,r,4,1,-1): return s
	return -1