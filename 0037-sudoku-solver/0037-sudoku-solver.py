class Solution:
    def solveSudoku(self, board):
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        # Step 1: Initialize
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty.append((i, j))
                else:
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[(i // 3) * 3 + (j // 3)].add(num)

        # Step 2: Backtracking using index
        def backtrack(index):
            if index == len(empty):
                return True

            i, j = empty[index]
            box_id = (i // 3) * 3 + (j // 3)

            for num in map(str, range(1, 10)):
                if num not in rows[i] and num not in cols[j] and num not in boxes[box_id]:

                    # place
                    board[i][j] = num
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[box_id].add(num)

                    if backtrack(index + 1):
                        return True

                    # undo
                    board[i][j] = '.'
                    rows[i].remove(num)
                    cols[j].remove(num)
                    boxes[box_id].remove(num)

            return False

        backtrack(0)