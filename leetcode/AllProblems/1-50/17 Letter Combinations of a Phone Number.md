## 17. Letter Combinations of a Phone Number

![image-20200418152526283](../../../.assert/image-20200418152526283.png)

给定一个电话号码上的数字组合，返回所有可能的字母组合。

## 回溯法

![image-20200418152425300](E:\OneDrive\笔记\.assert\image-20200418152425300.png)

遍历每个数组对应的字母，将其组合

~~~python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d2l = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8": "tuv",
            "9":"wxyz"
        }
        result = []
        for c in digits[::-1]:
            tmp = []
            letter = d2l[c]
            result = [c + l for c in letter for l in result]
        return result
~~~

时间复杂度为$O(3^M\times 4^N)$,M,N分别为对应3个和4个字母的数字数量，空间复杂度为$O(3^M\times 4^N)$