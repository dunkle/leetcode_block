class trie_tree:
    def __init__(self):
        self.tree_dict = {}
    def trie(self, word):
        temp = self.tree_dict
        for i in word:
            if i not in temp:
                temp[i] = {}
            temp = temp[i]
        temp['end'] = True
