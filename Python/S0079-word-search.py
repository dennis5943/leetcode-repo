"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

 
Constraints:
	board and word consists only of lowercase and uppercase English letters.
	1 <= board.length <= 200
	1 <= board[i].length <= 200
	1 <= word.length <= 10^3
"""
from typing import List
from copy import deepcopy
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # dfs
        def dfs(row: int, col: int, widx: int):
            # no character to find            
            if widx >= len(word): # check widx in bound of word
                return True
            elif row < 0 or row >= len(board) or col < 0 or col == len(board[0]): # check row,col in bound of board
                return False
            elif board[row][col] != word[widx]: 
                return False            
            
            board[row][col] = '#'

            for d in [[0,1],[0,-1],[1,0],[-1,0]]:
                if dfs(row + d[0],col + d[1], widx + 1):
                    return True
            board[row][col] = word[widx]
            
            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if dfs(i, j, 0):
                    return True
        return False


if __name__ == '__main__':
    board = [
        ["A","A","A","A","A","A"],
        ["A","A","A","A","A","A"],
        ["A","A","A","A","A","A"],
        ["A","A","A","A","A","A"],
        ["A","A","A","A","A","A"],
        ["A","A","A","A","A","A"]
    ]
    assert Solution().exist(deepcopy(board), "AAAAAAAAAAAABAA") == False

    board = [
        ["C","A","A"],
        ["A","A","A"],
        ["B","C","D"]
    ]
    
    assert Solution().exist(deepcopy(board), "AAB") == True

    board = [
        ['a']
    ]
    assert Solution().exist(deepcopy(board), "a") == True

    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    assert Solution().exist(deepcopy(board), "ABCCED") == True
    assert Solution().exist(deepcopy(board), "SEE") == True
    assert Solution().exist(deepcopy(board), "ABCB") == False
    assert Solution().exist(deepcopy(board), "ASAD") == True
    assert Solution().exist([["a","b"],["c","d"]], "acdb") == True
