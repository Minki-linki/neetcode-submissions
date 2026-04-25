class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        colums = [0] * 9
        squad = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue

                val = int(board[r][c])
                if (1<<val) & rows[r]:
                    return False
                if (1<<val) & colums[c]:
                    return False
                if (1<<val) & squad[(r//3)*3+(c//3)]:
                    return False
                
                rows[r] |= (1 << val)
                colums[c] |= (1 << val)
                squad[(r//3)*3+(c//3)] |= (1 << val)
        return True

