# Aug. 17, 2018

# Prints the integer (below the input integer) with the longest Collatz sequence.

import sys				# Imports sys module. We need to use exit() from it.

def collatz(n):			# This contains the code we need to use (call) again and again.
	if n % 2  == 0:
		return n // 2
	else:
		return 3 * n + 1

print('Enter a posivie integer and I will give you the integer below that no. whose collatz is longest.')

try:					# 'ValueError' problem fixed using try and except statements.
	n = int(input())	# Assign the integer to variable, n.
except ValueError:
	print('Only integers are acceptable.')
	sys.exit()			# We don't want program to continue if the ValueError occurs. So exit.

nextNumber = n

greater = 0
if nextNumber > 1:	# The if clause below runs only for positive integers. 
	while nextNumber > 1:
		n = nextNumber
		step = 0
		while n > 1:	
			step = step + 1
			n = collatz(n)
		
		# We keep comparing two 'step' variables & store grater value in variable, 'greater'. 
		if step > greater:	
			greater = step
			num_great = nextNumber	# 'numGreat' variable for the integer for which no. of steps in collatz is greater.
		else:		# This else is optional. We may skip it. But I prefer this way for clarity of what's happening.
			greater = greater
			num_great = num_great
		
		nextNumber = nextNumber - 1 

	print('The integer ' + str(num_great) + ' has the longest sequence with ' + str(greater) + ' no. of steps.')
		
if n < 1:
	print('Only positive integers have a Collatz sequence.')
	
# I am yet to study lists and dictionaries.