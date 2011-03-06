import sys
import getopt
from grid.grid import Grid
from grid.boxrenderer import BoxRenderer
from grid.textrenderer import TextRenderer
from helper import *



def run(boxes,options):
	#set the renderer
	print options
	print boxes
	if 'box' in options:
		_renderer = BoxRenderer()
	elif 'text' in options:
		_renderer = TextRenderer()


	#total area of all the boxes
	area = reduce(lambda i,j:i+j,map(lambda i:i[0]*i[1],boxes))

	#get the max width of the boxes 
	#make the the first height to test of the rectangle
	#this is becuase of the presorting in descending order
	width = boxes[0][0]

	#get the max length
	#used to show when to stop making rectangles to check
	max_length = max(map(lambda i:i[1],boxes))

	#find the height that 
	#is greater than or equal to the area of the boxes total area
	height = 0
	a = 0
	while height == 0:
		a=a+1
		if a*width >= area:
			height = a

	#some info for the user
	if 'verbose' in options:
		print "using boxes:"
		print boxes

		print "total area:"
		print area

		print "start with minimal width rectangle:"
		print (width,height)
	
	#initialize results
	#use maxint
	result = {'area':9999999999999,'dimensions':(0,0),'grid':None}

	
	
	initial_width = width
	initial_height = height
	#print max_length
	#main search loop
	print (width,height,max_length)
	while height >= max_length:
		
		#check to see if this rectangle is worth testing
		#it doesn't make sense to test a recntangle that is already larger
		#than our best.
		if (height*width)<=result['area']:
			
			if 'verbose' in options:
				print "testing:"
				print (width,height)
			
			#initiallize grid and run the main loop
			#if the boxes can't fit in the rectangle 
			#increase the height until the boxes fit
			g = Grid(height,width)
			if 'recursive' in options:
				while g.placeRecursively(boxes,0) != True:
					g = Grid(width,g.l+1)
			elif 'greedy' in options:				
				while g.placeGreedily(boxes) != True:
					g = Grid(width,g.l+1)
				
			#set the renderer and display info for the user	
			g.setRenderer(_renderer)
			
			if 'verbose' in options:
				print "found the following:"
				g.display()
				print "containing rectangle:"
				print (g.l,g.w)
				print "area of rectangle:"
				print g.l*g.w
			if result['area'] > g.l*g.w:
				result['area'] = g.l*g.w
				result['dimensions'] = (g.l,g.w)
				result['grid'] = g
		
		#increase the width
		#minimize height which is also
		#greater than the area of the boxes	

		#this needs work
		width=width+1
		a=0
		while width*a < area:
			a=a+1
		height=a
		if height==1:
			height=0
		
	result['grid'].display()
	print result['area']

def main():
	
	opts = sys.argv[1:]
	options = ['greedy','text']
	if '-v' in opts:
		options.append('verbose')
	if '-b' in opts:
		options.append('box')
	if '-r' in opts:
		options.append('recursive')
	if '-t' in opts:
		options.append('text')
	if '-g' in opts:
		options.append('greedy')
	if '-random' in opts:
		options.append('random')
	
		
	boxes = []
	
	
	if 'random' in options:
		boxes = generateRandomBoxes()
	else:
		#get the number of boxes from stdin
		number = False
		while number == False:
			try:
				number = int(sys.stdin.readline())
				if number < 0:
					raise Exception()
			except:
				print 'please enter a whole number less than 100 and greater than 0.'
	
		#get the boxes from stdin
		for i in range(number):
			oktogo = False
			while oktogo == False:
				try:
					box = sys.stdin.readline()
					box = map(lambda i:int(i.strip()),box.split(' '))

					if box[0] <= 0:
						raise Exception()
					if box[1] <= 0:
						raise Exception()
					oktogo = True
				except:
					print 'please enter box dimensions with whole and positive numbers seperated by a single space.'
		
			box = (max(box),min(box))
			boxes.append(box)
		boxes.sort()
		boxes.reverse()
		
	run(boxes,options)
	
if __name__ == '__main__':
	main()


