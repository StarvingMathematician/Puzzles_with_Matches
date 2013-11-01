Puzzles_with_Matches
====================

Automatically solves "Number" levels from the Android game "Puzzles with Matches". These levels begin with a simple addition or subtraction equation where the numbers and operator are made up of matchsticks. The goal is to rearrange the matchsticks in only 1 or 2 moves (as specified by the level's instructions) to obtain an arithmetically correct expression. In the example seen [here](http://cdn8.staztic.com/app/a/2431/2431270/puzzles-with-matches-13-0-s-307x512.jpg), we would move the bottom-left match from the 6 to the top-right position on the 6, yielding the correct expression "9 + 0 = 9".

There are two program files:

1. "generate_solution.py" -- When run, it prompts the user for the number of moves, and the initial equation. It then outputs the arithmetically correct final equation, from which the user can easily surmise the moves that need to be made.
2. "helper_functions.py" -- Contains functions which are called by "generate_solution.py". These include basic input/output routines as well as methods for getting/setting problem-specific parameters.
