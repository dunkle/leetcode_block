import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:

        def addword(word):
            if word not in wordId:
                nonlocal nodeNum # 设置一个局部函数的局部变量，其他局部函数都可以使用
                wordId[word] = nodeNum
                nodeNum+=1 # 给每个word编号
        def addEdge(word):
            '''
            可以理解为为一个节点创建相邻节点，相邻节点为用 * 替换掉任意一个字母位置的节点
            :param word:
            :return:
            '''
            addword(word)
            id1 = wordId[word]
            chars = list(word)  # 依次取word的每个字符作为char
            for i in range(len(chars)):
                tmp = chars[i]
                chars[i] = '*'
                newWord = "".join(chars) #把多个 单个字符拼接为一个字符串
                addword(newWord)
                id2 = wordId[newWord]
                edge[id1].append(id2)
                edge[id2].append(id1)
                chars[i] = tmp

        #先构造一个wordid 对应每一个单词, 构造一个节点连接的多个节点
        wordId = dict()
        nodeNum = 0
        edge = collections.defaultdict(list) # key 对应的 value值默认为list类型

        # 针对所有的wordList 构造一个无向图
        for word in wordList:
            addEdge(word)

        # 对输入的起始单词加入无向图, 结束的单词判断是否在图里，不在图里无法达到.
        print(edge)
        addEdge(beginWord)
        print(edge)
        if endWord not in wordId:
            return 0
        print(wordId)
        # 初始化所有 点之间的距离
        dis = [float("inf")] * nodeNum
        print(dis)

        beginId, endId = wordId[beginWord], wordId[endWord]
        dis[beginId] = 0
        que = collections.deque([beginId])
        while que:
            x = que.popleft()
            print('x',x)
            if x==endId:
                return dis[endId]//2 +1
            for it in edge[x]:
                # bfs 判断 与节点x 相连的节点有没有被遍历，没有被遍历说明距离无穷,此时更新该节点距离
                if dis[it] == float("inf"):
                    dis[it] = dis[x]+1
                    que.append(it)
        return 0

if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    solution = Solution()
    res = solution.ladderLength(beginWord, endWord, wordList)
    print(res)

