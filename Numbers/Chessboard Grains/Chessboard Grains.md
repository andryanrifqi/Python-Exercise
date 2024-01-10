Instructions
Calculate the number of grains of wheat on a chessboard given that the number on each square doubles.

There are 64 squares on a chessboard (where square 1 has one grain, square 2 has two grains, square 3 has four grains, and so on).

Write code that shows:

how many grains were on a given square, and
the total number of grains on the chessboard

Exception messages

Eaise statement to "throw" a ValueError when the square input is out of range. The tests will only pass if you both raise the exception and include a message with it.

To raise a ValueError with a message, write the message as an argument to the exception type:

# when the square value is not in the acceptable range        
raise ValueError("square must be between 1 and 64")