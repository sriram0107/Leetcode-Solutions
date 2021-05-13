
class Solution:
    count = 0
    def totalNQueens(self, n: int) -> int:
        board = [[0 for j in range(n)] for i in range(n)]        
        self.solveForQueens(board,0,n)
        return self.count
    
    def solveForQueens(self,board,row,n):
            if row>=n:
                self.count+=1
                return
            for i in range(n):
                if self.isSafe(board,row,i,n):
                    board[row][i] = 1
                    self.solveForQueens(board,row+1,n)
                    board[row][i] = 0
    
    
    def isSafe(self,board,i,j,n):
        for x in range(n): #check column
            if board[x][j]==1 and x!=i:
                return False
        #check right diag
        for x in range(n):
            for y in range(n):
                if x+y==i+j and x!=i and y!=j and board[x][y]==1:
                    return False
        #check left diag
        for x in range(n):
            for y in range(n):
                if x-y==i-j and x!=i and y!=j and board[x][y]==1:
                    return False
        
        return True
        
            
        
 
    
    