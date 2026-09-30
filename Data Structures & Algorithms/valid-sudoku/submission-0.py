from collections import Counter
from typing import List

class Solution:
    def has_no_duplicates(self, freq_dict: dict) -> bool:
        return max(freq_dict.values(), default=0) <= 1

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. Check all 9 3x3 grids
        for x in (0, 3, 6):
            for y in (0, 3, 6):
                # Corrected 2D array indexing syntax
                grid = [
                    board[x+0][y+0], board[x+0][y+1], board[x+0][y+2],
                    board[x+1][y+0], board[x+1][y+1], board[x+1][y+2],
                    board[x+2][y+0], board[x+2][y+1], board[x+2][y+2]
                ]
                frequencyDict = dict(Counter(grid))
                frequencyDict.pop(".", None)  # Safely removes '.' without KeyError
                
                # If has_no_duplicates returns False, there IS a duplicate
                if not self.has_no_duplicates(frequencyDict):
                    return False

        # 2. Check all horizontal rows and vertical columns
        for index in range(9):
            horizontalRow = board[index]
            verticalColumn = [board[r][index] for r in range(9)]  # Corrected column extraction

            frequencyDict1 = dict(Counter(horizontalRow))
            frequencyDict1.pop(".", None)
            
            frequencyDict2 = dict(Counter(verticalColumn))
            frequencyDict2.pop(".", None)

            if not self.has_no_duplicates(frequencyDict1) or not self.has_no_duplicates(frequencyDict2):
                return False

        return True