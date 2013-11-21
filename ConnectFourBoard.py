class ConnectFourBoard:
	boardColumns=7
	boardRows=6

	def __init__(self):
		self.grid=[[] for _ in range(ConnectFourBoard.boardColumns)]

	def __str__(self):
		s = "---------\n"
		for i in range(ConnectFourBoard.boardRows-1,-1,-1):
			s+="|"
			for j in range(ConnectFourBoard.boardColumns):
				if i<len(self.grid[j]): s+=str(self.grid[j][i])
				else: s+=" "
			s+="|\n"
		s+="---------\n"
		s+=" 0123456 "
		return s

	def move(self, col, player):
		if col<0 or col>=ConnectFourBoard.boardColumns:
			raise Exception("column out of range")
		elif not (player==0 or player==1): raise Exception("invalid player")
		elif len(self.grid[col])>=ConnectFourBoard.boardRows:
			raise Exception("column is full")

		self.grid[col].append(player)

	def height(self, col):
		return len(self.grid[col])

	def pos(self,col,row):
		#print col,row
		if row>=0 and row<len(self.grid[col]): c=self.grid[col][row]
		else: c=-1

		return c

	def section(self, col, row, length, hStep, vStep):
		sec=[]
		for i in range(length):
			#print col+i*hStep,row+i*vStep
			sec.append(self.pos(col+i*hStep,row+i*vStep))
		return sec

	def cols(self):
		return ConnectFourBoard.boardColumns

	def rows(self):
		return ConnectFourBoard.boardRows;