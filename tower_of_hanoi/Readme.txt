Problem Description :

		The Tower of Hanoi (also called the Tower of Brahma or Lucas' Tower[1] and sometimes pluralized as Towers) is a mathematical game or puzzle. It consists of N Towers and M number of disks of different sizes, which can slide onto any tower. The puzzle starts with the disks in a neat stack in ascending order of size on one tower, the smallest at the top, thus making a conical shape.

		The objective of the puzzle is to move the entire stack to another tower, obeying the following simple rules:

			1. Only one disk can be moved at a time.
			2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
			3. No larger disk may be placed on top of a smaller disk.

Requirements to Execute :

		Any Python Runnable IDE 

Steps to Execute :

		1. Open terminal 
		2. Navigate to the respective folder 
		3. use the following command 

			Python3 filename.py (no.of Discs) (no. of towers)

Sample input:

	Input Parameters : 

		1. No. of Tower
		2. No. of Discs

	Python3 hanoi-nk.py 3 2

Sample output:

		['D1', 'D2', 'D3']
		[]
		[]
		[]

		['D2', 'D3']
		[]
		[]
		['D1']

		['D3']
		[]
		['D2']
		['D1']

		[]
		['D3']
		['D2']
		['D1']

		[]
		['D2', 'D3']
		[]
		['D1']

		[]
		['D1', 'D2', 'D3']
		[]
		[]

		total moves = 5


