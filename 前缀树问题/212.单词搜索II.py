'''
212. 单词搜索 II
给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words，找出所有同时在二维网格和字典中出现的单词。

单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

示例 1：
输入：board = [["o","a","a","n"],
            ["e","t","a","e"],
            ["i","h","k","r"],
            ["i","f","l","v"]], words = ["oath","pea","eat","rain"]
输出：["eat","oath"]
示例 2：


输入：board = [["a","b"],["c","d"]], words = ["abcb"]
输出：[]


提示：

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] 是一个小写英文字母
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] 由小写英文字母组成
words 中的所有字符串互不相同
'''
class Solution:
    def findWords(self, board, words):
        self.res = []
        self.trie_tree = {}

        if not board:
            return self.res

        # 首先构造一棵前缀树，为了避免 words里的单词有相同前缀的被重复搜索
        # 依次将每个单词 存入前缀树
        for word in words:
            self.trie_tree_construct(word)
        print(self.trie_tree)
        m = len(board)
        n = len(board[0])
        # 构造一个访问列表，避免回溯的时候反复访问同一个节点
        visit = [[0 for i in range(n)] for j in range(m)]

        # 依次找board 里的每个字母，如果字母出现在前缀树的首字母里，则以该字母进行dfs搜索
        # 查看是否符合前缀树里的单词
        for i in range(m):
            for j in range(n):
                if board[i][j] in self.trie_tree:
                    self.dfs(i, j, board, self.trie_tree, visit)
        return self.res
        # return list(set(self.res))

    def trie_tree_construct(self, word):
        temp = self.trie_tree
        for i in word:
            if i not in temp:
                temp[i] = {}
            temp = temp[i]
        temp["end"] = word

    def dfs(self, i, j, board, tmp_trie_tree, visit):
        # print(tmp_trie_tree)
        # 如果遍历的字母 出现在 前缀树里，说明可以继续往上下左右扩散找单词
        if board[i][j] in tmp_trie_tree:
            # 找过的标记为1
            visit[i][j] = 1
            # 字典树往前推进一格
            tmp_trie_tree = tmp_trie_tree[board[i][j]]
            # 推进到，如果出现end， 说明是有一个单词了,说明到此可以组成一个单词
            # 但是此处仍然可以往下搜索，是否继续存在单词，因此只需把对应的end位置的单词置为一个标志符
            # 标识符仍然可以起到去重复的作用
            if 'end' in tmp_trie_tree and tmp_trie_tree["end"]!=0:
                self.res.append(tmp_trie_tree["end"])
                tmp_trie_tree["end"] = 0
            steps = [(-1,0), (1, 0), (0, 1), (0, -1)]
            for step in steps:
                x = i + step[0]
                y = j + step[1]
                if 0<=x<len(board) and 0<=y<len(board[0]) and visit[x][y]==0:
                    self.dfs(x, y, board, tmp_trie_tree, visit)
            visit[i][j] = 0
        else:
            return
a =  Solution()
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]

# board = [["a"]]
# board = [["a", "b"]]

# words = ["a"]

board = [["a","b","c"],["a","e","d"],["a","f","g"]]
words = ["abcdefg","gfedcbaaa","eaabcdgfa","befa","dgc","ade", "abcde"]
# words = ["dgc"]
res = a.findWords(board,words)
print(res)


