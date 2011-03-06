This is my response to the dropbox box challenge here:
http://www.dropbox.com/jobs/challenges


Syntax:
python getrectanglecontainer.py [options]
	1. Enther number of boxes to be used
	2. Enter the dimensions of those boxes

Sample Input
3
8 8
3 4
4 3


Options:
	-v verbose mode
	
	-b box drawing mode (super cool, requires Latin-US(Dos) character set)
	
	-t (default) text drawing mode
	
	-g (default) greedy placement of boxes
	
	-r recursive/exhaustive placement of boxes (slow)
	
	-random automatically choses a random number and random sized boxes for you

Best if used like:
	(set your terminal to use Latin-US(dos))
	python getrectanglecontainer.py -random -box


Copy of text from the orginal problem:
When you're working with petabytes of data, you have to store files wherever they can fit. All of us here at Dropbox are always searching for more ways to efficiently pack data into smaller and more manageable chunks. The fun begins when you bend the rules a little bit and visualize it in two dimensions.

You'll be given a list of rectangular "files" that you'll need to pack into as small a "Dropbox" as possible. The dimensions of each file will be specified by a tuple (width, height), both of which will be integers. The output of your function should be the area of the smallest rectangular Dropbox that can enclose all of them without any overlap. Files can be rotated 90° if it helps. Bonus points if you can draw pictures of the winning configurations along the way. While drawing pictures, any files sharing dimensions should be considered identical/interchangeable.

Input
Your program must read a small integer N (1 <= N <= 100) from STDIN representing the maximum number of files to consider, followed by the width and height of each file, one per line.

Output
Output should be simply be the area of the smallest containing Dropbox. If you want to print pretty pictures, send that to stderr. Only the output on stdout will be judged.
