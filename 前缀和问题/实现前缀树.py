class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        t = self.dict
        for i in word:
            if i not in t:
                t[i] = {} # 一个word 插入，如果当前字母不在字典里则 添加该字母，并且以该字母新建一个字典索引嵌套
            t = t[i]    # 一个word 插入，如果当前字母在索引里了，那么以当前字母递归，也就是接着这个字母往后插入
                        # 此时需要更改字典集合t 为 以当前字母 i为根字母的 子字典集合
        t['end'] = True # 在每个单词插入完之后，插入标志符

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        t = self.dict
        for i in word:
            if i in t:
                t = t[i]
            else:
                return False
        return 'end' in t


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        t = self.dict
        for i in prefix:
            if i in t:
                t = t[i]
            else:
                return False
        return True


'''
该数据结构 搜索引擎的关键词提示功能，以及 IDE 的自动补全功能
'''

# Your Trie object will be instantiated and called as such:
word = 'start'
prefix = 'sta'
obj = Trie()
obj.insert(word)
obj.insert('stassha')

param_2 = obj.search(word)
param_3 = obj.startsWith(prefix)
print(obj.dict)
