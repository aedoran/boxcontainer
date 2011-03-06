import sys
class Grid:

	def __init__(self,w,l):
		self.box = self.createEmptyGrid(w,l)
		self.l = l
		self.w = w
	
	def setRenderer(self,renderer):
		self.renderer = renderer
		
	def display(self):
		"""display method.  Should only be called after the renderer is called."""
		self.renderer.display(self.renderer,self.box)
	
	
	def placeGreedily(self,boxes):
		"""This function does a very greedy placement of boxes while also 
		checking the 90 degree rotation"""
		
		#find a better way to map the array
		#used to keep track of the boxes that are placed
		_boxes = []
		for i in range(len(boxes)):
			_boxes.append((i,boxes[i]))
			
			
		for x in range(self.w):
			for y in range(self.l):
				for b in _boxes:
					box_width = b[1][0]
					box_length = b[1][1]
					box_id = b[0]+1  #need to make sure that the id is not zero
					if self.placeBox(x,y,box_width,box_length,box_id):
						_boxes.remove(b)
					elif self.placeBox(x,y,box_length,box_width,box_id):
						_boxes.remove(b)
		
		#if all the boxes are placed we are done
		if len(_boxes) == 0:
			return True
		else:
			return False
		
	def placeRecursively(self,boxes,c):
		"""This is a much more thorough, and extremely slow way to place the boxes."""
		done = False
		b = boxes[c]
		b_width = b[0]
		b_length = b[1]
		
		#used to stop the box from testing overlaps, and still allowing to test the rotation
		small_side = min(b)
		for x in range(self.w-small_side+1):
			for y in range(self.l-small_side+1):
				if self.placeBox(x,y,b_width,b_length,str(c+1)):
						
					if c==len(boxes)-1:
						return True
					else:
						done = self.placeRecursively(boxes,c+1)
						if done == False:
							self.removeBox(x,y,b_width,b_length)

				#rotation placement
				elif self.placeBox(x,y,b_length,b_width,str(c+1)):
					if c==len(boxes)-1:
						return True
					else:
						done = self.placeRecursively(boxes,c+1)
						if done == False:
							self.removeBox(x,y,b_length,b_width)


		return done
		
	def createEmptyGrid(self,w,l):
		"""initializes the grid with zeroes."""
		g = []
		for a in range(l):
			g2 = []
			for b in range(w):
				g2.append(0)
			
			g.append(g2)
		
		return g
	
	def removeBox(self,boxX,boxY,boxW,boxL):
		"""simply remove a box from the grid."""
		for a in range(boxL):
			for b in range(boxW):
				self.box[boxY+a][boxX+b] = 0
	


	def placeBox(self,boxX,boxY,boxW,boxL,boxId):
		"""Places a box at boxX,boxY in the grid and writes the boxId into the grid.
		returns true if successful, flase if it couldn't be placed"""

		#grid
		gridL = len(self.box)
		gridW = len(self.box[0])
		
		#test if box is trying to be placed out of the grid
		if gridL<boxY+boxL:
			return False
		
		if gridW<boxX+boxW:
			return False


		#test if box is trying to be placed on another box
		for a in range(boxL):
			for b in range(boxW):
				if self.box[boxY+a][boxX+b] != 0:
					return False 
		
		#place the box
		for a in range(boxL):
			for b in range(boxW):
				self.box[boxY+a][boxX+b] = boxId
		
		return True
				

