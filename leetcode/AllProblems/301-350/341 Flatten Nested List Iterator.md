# 341. Flatten Nested List Iterator

![image-20200411184657514](../../.assert/image-20200411184657514.png)

~~~python
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        
        def flatten_list(nestedList: [NestedInteger]):
            l = []
            for ni in nestedList:
                if ni.isInteger():
                    l.append(ni.getInteger())
                else:
                    l.extend(flatten_list(ni.getList()))
            return l
        
        
        self.l = flatten_list(nestedList)
        self.i = 0
    
    def next(self) -> int:
        v = self.l[self.i]
        self.i += 1
        return v
    
        
    
    def hasNext(self) -> bool:
         return self.i < len(self.l)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
~~~

