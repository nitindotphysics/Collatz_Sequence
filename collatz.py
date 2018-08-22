# Prints the Collatz sequence for the input positive integer.

import sys			# Imports sys module. We need to use exit() from it.

def collatz(n):			# This contains the code we need to use (call) again and again.
	if n % 2  == 0:
		print(n // 2)
		return n // 2
	else:
		print(3 * n + 1)
		return 3 * n + 1

print('Enter a posivie integer and I will print the Collatz sequence.')		# Ask the user to enter the integer whose collatz they need.

try:				# 'ValueError' problem fixed using try and except statements.
	n = int(input())	# Assign the integer to variable, n.
except ValueError:
	print('Only integers are acceptable.')
	sys.exit()		# We don't want program to continue if the ValueError occurs. So exit.

step = 0			# Initialize the variable, step.
if n > 1:			# We need to execute 'while', only for positive integers.
	while n > 1:			# Call collatz function again and again with previous return value as the new parameter.
		step = step + 1		# With each pass (iteration), variable, step increased by 1.
		n = collatz(n)
	print('This sequence has ' + str(step) + ' steps.')	# Prints only AFTER while loop ends. (This is inside 'if clause' & outise 'while clause'.)

	
if n < 1:		# This executes when user enters a negative integer.
	print('Only positive integers have a Collatz sequence.')
