class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                box = board[r][c]

                if box == ".":
                    continue

                if (
                    box in rows[r] or
                    box in cols[c] or 
                    box in squares[(r // 3, c // 3)]
                ):
                    return False

                rows[r].add(box)
                cols[c].add(box)
                squares[(r // 3, c // 3)].add(box)

        return True

# time: O(n ^ 2)
# space: O(1)
