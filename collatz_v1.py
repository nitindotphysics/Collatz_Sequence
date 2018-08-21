# Program to print the Collatz sequence for an input integer.

def collatz(n):			# This contains the code we need to use (call) again and again.
	if n % 2  == 0:
		print(n // 2)
		return n // 2
	else:
		print(3 * n + 1)
		return 3 * n + 1

print('Enter a posivie integer.')	 # Ask user to enter the positive integer whose collatz they need.
n = int(input())		         # Assign that integer to variable, n. 

while n != 1:			         # Call collatz function again and again with its previous return value as new parameter.
	n = collatz(n)
	

# Problems: If integer entered is negative, program run into infine loop. Fixed in next version.
