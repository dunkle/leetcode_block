给定一个包含字母的矩阵，判断单词是否在矩阵中

可以将访问过的字符置为#,就不用记录是否访问过。

~~~python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        
        if not board or not board[0]:
            return False
        
        m, n = len(board), len(board[0])
        
        def dfs(x, y, word):
            if len(word) == 0:
                return True
            
            if x < 0 or x >= m or y < 0 or y >= n or word[0] != board[x][y]:
                return False
            
            tmp = board[x][y]
            board[x][y] = '#'
            
            result = dfs(x+1, y, word[1:]) or dfs(x, y+1, word[1:]) or dfs(x-1, y, word[1:]) or dfs(x, y-1, word[1:])
            board[x][y] = tmp
            
            return result
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, word):
                    return True
                
        return False
        
        
~~~

