# Program to print the Collatz sequence.

def collatz(n):			# This contains the code we need to use (call) again and again.
	if n % 2  == 0:
		print(n // 2)
		return n // 2
	else:
		print(3 * n + 1)
		return 3 * n + 1

print('Enter a posivie integer and I will print the Collatz sequence.')	# Ask user to enter integer whose collatz they need.
n = int(input())		# Assign that integer to variable, n.

while n > 1:			# Call collatz function again and again with previous return value as the new parameter.
	n = collatz(n)
	
	
# Problems: Now, on entering negative integers, no infinite loop, but does...
# nothing either. Fixed in the next version.
