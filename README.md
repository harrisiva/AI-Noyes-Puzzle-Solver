# AI Noyes Puzzle Solver
## Overview
The goal of this project was to test the performance of three different heuristics for solving a
NxN puzzle using an A* search algorithm. The code was written in Python, with the additional
use of modules such as numpy. The reason numpy was chosen is because numpy, unlike python
lists, stores elements in adjacent memory locations. Therefore, this package was chosen to
mainly hold the state (board and puzzle pieces).
## Heuristics
Since h3 was the only heuristic that was not provided, we will elaborate on it in this section. The
h3 heuristic was taken from https://cse.iitk.ac.in/users/cs365/2009/ppt/13jan_Aman.pdf.
This heuristic finds the number of misplaced tiles based on their given row and column. For
example, given a 3x3 puzzle with the tiles 1 and 2 associated to R0C1 and R0C2, for any
displacement from their respective row and columns, the value of the displacement would be
added to the heuristic. Since it just takes in account rows and columns it works for both 3x3 and
4x4. h3 would be considered admissible since to solve the puzzle if there are tiles in the wrong
column or tile, they must move at least once to get to their goal state. This means that the cost to
reach the goal state will always be at least as much as the estimated cost or more, therefore h3
would be an admissible heuristic.

Given the current state: [[7, 2, 4],[5, 0, 6],[8, 3, 1]].
- The h3 would be 5 + 8 so 13. This is because there are 5 tiles that are in the wrong row
and there are 8 tiles that are in the wrong column.

See another example: [[2, 1, 0], [3, 4, 5], [6, 7, 8]]
- h3 would equal 1 because only tile 2 is in the wrong column and everything is in the
right row.

An example for 4x4: [[0, 1, 2, 4], [3, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]].
- h3 for this would be 2 + 2 = 4 since both tile 4 and 3 are in the wrong row and column.
