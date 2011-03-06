import sys
class TextRenderer:
	def display(grid,self,box):
		for x in range(len(box)):
			a = ''
			line = map(lambda a:str(a),box[x])
			print >> sys.stderr, a.join(line)
				