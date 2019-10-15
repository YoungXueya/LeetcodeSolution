class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        table=set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]!='.':
                    if str(board[i][j])+'col'+str(j) in table or str(board[i][j])+'row'+str(i) in table or str(board[i][j])+'cube'+str(i//3)+str(j//3) in table:
                            return False
                    else:
                        table.add(str(board[i][j])+'col'+str(j))
                        table.add(str(board[i][j])+'row'+str(i))
                        table.add(str(board[i][j])+'cube'+str(i//3)+str(j//3))
        return True
                        
        
