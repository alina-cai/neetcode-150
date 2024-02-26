class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                square = board[r][c]

                if square == ".":
                    continue

                if (
                    square in rows[r] or 
                    square in cols[c] or
                    square in squares[(r // 3, c // 3)]
                ):
                    return False

                rows[r].add(square)
                cols[c].add(square)
                squares[(r // 3, c // 3)].add(square)

        return True
    
# time: O(n ^ 2)
# space: O(1)
