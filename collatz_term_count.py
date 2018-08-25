
# Prints no. of steps in Collatz sequence for all postive integers less than and equal to the input no.

import sys      	# Imports sys module. We need to use exit() from it.

def collatz(n): 	# This contains the code we need to use (call) again and again.
	if n % 2  == 0:
		return n // 2
	else:
		return 3 * n + 1

print('Enter a posivie integer and I\'ll give you steps in collatz for all integers below it.')

try:					# 'ValueError' problem fixed using try and except statements.
	n = int(input())		# Assign the integer to variable, n.
except ValueError:
	print('Only integers are acceptable.')
	sys.exit()			# We don't want program to continue if the ValueError occurs. So exit.

# We need two while loops:
# First to find no. of steps in collatz of a particular integer, see n below; 
# and the 2nd loop to repeat this whole process on integer one less than previous integer, see 'nextNumber' below.  

nextNumber = n    	# Both n and nextNumber equal initially. We start counting terms in collatz from the input integer & go down to 1.

while nextNumber > 1:		# This 'master while' runs only for positive integers. 
	n = nextNumber 		# The 'nextNumber' from last line of 'master while' fed to n as now we need to do 2nd 'while' on that no.
	step = 0
	
	# The 'while' below is to get the no. of steps in collatz sequence of integer n.
	while n > 1:		# Call collatz(n) again & again with its previous return value as new parameter. 
		step = step + 1 # Counts no. of terms (steps) in collatz for integer n.
		n = collatz(n)
	
	print(str(nextNumber) + ' has ' + str(step) + ' no. of steps in its collatz')
	nextNumber = nextNumber - 1 
	
if n < 1:		# This executes when user enters a negative integer.
	print('Only positive integers have a Collatz sequence.')
	
# Important: One thing to notice is the use of two while loops. If we use a formula to directly count the no. of steps in collatz of an integer,
# we could have avoided the 2nd loop. But I am not sure whether such a formula still exists in maths literature. So I preferred to use 2nd while loop.
# Here in the 2nd 'while', we take the no. n and generate succesive integers in it's collatz sequence by calling collatz(n) again and again on ...
# the previous generated term in the sequennce until we get 1. Now insted of printing the whole sequence, we just count the steps in it and prints it.
# That does the job and we repeat the same with 'master while' on integers one less than the previous integer on which we just have counted steps.
