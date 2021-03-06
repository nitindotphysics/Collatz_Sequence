
# Collatz Sequence

Collatz Sequence problem is a famous unsolved mathematics problem named after mathematician Lothar Collatz. In this project, I tried to study the same using Python. This is the 1st project in my *Beginner_Python_Projects series*.

## Theory

Think of a positive integer. If the integer is even, divide it in half. If it is odd, multiply it by 3 and add 1. Repeat the operation on each successive result and keep doing that until you get 1. The sequence generated by this operation is the Collatz Sequence.

The operation can be written as the following function:

![](http://latex.codecogs.com/gif.latex?f%28n%29%3D%20%5Cbegin%7Bcases%7D%20n/2%20%2C%26n%3D%20even%20%263n&plus;1%2C%26n%3D%20odd%20%5Cend%7Bcases%7D)

And repeat the operation with each successive result as the new variable for function ![](http://latex.codecogs.com/gif.latex?f%28n%29),  i.e.  ![](http://latex.codecogs.com/gif.latex?n%20%3D%20f%28n%29)

The beauty of this problem is that no matter which integer (positive) you start with, with the operation mentioned above, you always end up at 1. This is the famous Collatz conjecture. Nobody can prove this yet. In the words of mathematician Jeffrey Lagarias:
> This is an extraordinarily difficult problem, completely out of reach of present day mathematics.

Know more about Collatz Sequence [here](https://en.wikipedia.org/wiki/Collatz_conjecture#See_also).

## What programs do

I wrote three python programs on Collatz: 

1.	**collatz.py**
This is the basic program where user inputs a positive integer whose Collatz sequence they want and the program prints the sequence for them along with the total no. of steps (terms) in that sequence.

2. **collatz_term_count.py**
User can enter a positive integer and the program prints the no. of steps (terms) in the Collatz of that integer and every positive integer below it.  

3. **longest_collatz.py**
User enters a positive integer and the program gives the integer below that input integer whose Collatz has the largest no. of steps (terms) and prints the no. of steps (terms) for the same.

## Python Concepts Used

- Variables;
- Flow Control Statements;
- Loops;
- Def statements;
- Try, except and return statements.

## Further reading

There is much more to Collatz Conjecture. I think we can do many interesting things in Collatz using Python. So in future, I plan to dig deeper into its theory and see what else I can do in Collatz using Python/Coding.

## Requests

I used commenting a lot in each program to make it more readable and comprehensible to people. This may help beginners, but perhaps, a lot of commenting may do the opposite than intended. Please tell me if that is the case. 

If you have any feedback/criticism/advice for me related to this project, feel free to comment/review. It would mean a lot to me. You can contact me on [twitter](https://twitter.com/NKakria) too.

## References

- Automate the Boring Stuff with Python
- Wikipedia

