class BoxRenderer:
	def displayBoxCharacter(self,up,down,left,right):

		#
		#		197 up/down/left/right
		#		
		#		180 up/down/left
		#		195 up/down/right
		#		194 left/right/down
		#		193 left/right/up
		#		
		#		179 up/down
		#		196 left/right
		#		
		#		191 left/down
		#		192 up/right
		#		217 left/up
		#		218 right/down

		if up and down and left and right:
			return chr(197)
		elif up and down and left:
			return chr(180)
		elif up and down and right:
			return chr(195)
		elif up and right and left:
			return chr(193)
		elif down and right and left:
			return chr(194)
		elif up and down:
			return chr(179)
		elif left and right:
			return chr(196)
		elif up and right:
			return chr(192)
		elif up and left:
			return chr(217)
		elif down and right:
			return chr(218)
		elif down and left:
			return chr(191)

	def display(grid,self,box):
		self.dBox(box)

	def dBox(self,box):
		x = box
		l = len(x)
		w = len(x[0])
		for a in range(l+1):
			line = ''
			for b in range(w+1):

				if a > 0 and b > 0 and b != w and a != l:
					#internal points
					nw = x[a-1][b-1]
					ne = x[a-1][b]
					sw = x[a][b-1]
					se = x[a][b]
					if nw == ne and ne == se and se == sw:
						line += ' '
					elif nw != ne and ne != se and se != sw and sw != nw:
						line += self.displayBoxCharacter(True,True,True,True)
					elif nw != ne and ne == se and se == sw:
						line += self.displayBoxCharacter(True,False,True,False)
					elif ne != nw and nw == sw and sw == se:
						line += self.displayBoxCharacter(True,False,False,True)
					elif se != sw and sw == nw and nw == ne:
						line += self.displayBoxCharacter(False,True,False,True)
					elif se != sw and se == nw and nw == ne:
						line += self.displayBoxCharacter(False,True,True,False)
					elif nw == ne and se == sw and nw != sw:
						line += self.displayBoxCharacter(False,False,True,True)
					elif nw == sw and se == ne and se != sw:
						line += self.displayBoxCharacter(True,True,False,False)
					elif nw == sw and se != ne and se != sw and ne != nw:
						line += self.displayBoxCharacter(True,True,False,True)
					elif nw == ne and se != sw and ne != se and sw != nw:
						line += self.displayBoxCharacter(False,True,True,True)
					elif ne == se and se != sw and sw != nw and ne != nw:
						line += self.displayBoxCharacter(True,True,True,False)
					elif sw == se and se != ne and ne != nw and nw != sw:
						line += self.displayBoxCharacter(True,False,True,False)

				elif a == 0 and b == 0:
					line += self.displayBoxCharacter(False,True,False,True)
				elif a == 0 and b != w:
					if x[a][b] == x[a][b-1]:
						line += self.displayBoxCharacter(False,False,True,True)
					else:
						line += self.displayBoxCharacter(False,True,True,True)
				elif b == 0 and a != l:
					if x[a][b] == x[a-1][b]:
						line += self.displayBoxCharacter(True,True,False,False)
					else:
						line += self.displayBoxCharacter(True,True,False,True)
				elif b == w and a == l:
					line+= self.displayBoxCharacter(True,False,True,False)
				elif b == w:
					if a == 0:
						line += self.displayBoxCharacter(False,True,True,False)
					elif x[a-1][b-1] != x[a][b-1]:
						line += self.displayBoxCharacter(True,True,True,False)
					else:
						line+= self.displayBoxCharacter(True,True,False,False)
				elif a == l:
					if b == 0:
						line += self.displayBoxCharacter(True,False,False,True)
					elif x[a-1][b] != x[a-1][b-1]:
						line += self.displayBoxCharacter(True,False,True,True)
					else:
						line+= self.displayBoxCharacter(False,False,True,True)


			print line