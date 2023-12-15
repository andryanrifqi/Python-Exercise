Instructions
The Collatz Conjecture or 3x+1 problem can be summarized as follows:

Take any positive integer n. If n is even, divide n by 2 to get n / 2. If n is odd, multiply n by 3 and add 1 to get 3n + 1. Repeat the process indefinitely. The conjecture states that no matter which number you start with, you will always reach 1 eventually.

Given a number n, return the number of steps required to reach 1.

Examples
Starting with n = 12, the steps would be as follows:

12
6
3
10
5
16
8
4
2
1
Resulting in 9 steps. So for input n = 12, the return value would be 9.

Exception messages

The Collatz Conjecture is only concerned with strictly positive integers, so this exercise expects you to use the raise statement and "throw" a ValueError in your solution if the given value is zero or a negative integer. The tests will only pass if you both raise the exception and include a message with it.

To raise a ValueError with a message, write the message as an argument to the exception type:

# example when argument is zero or a negative integer
raise ValueError("Only positive integers are allowed")