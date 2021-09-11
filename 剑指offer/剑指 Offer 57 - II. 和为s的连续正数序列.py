'''
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

 

示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]
示例 2：

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
 

限制：

1 <= target <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def findContinuousSequence(self, target: int):
        i = 1
        j = 2
        now = i
        res = []
        tmp = [i]
        while i<j and j<=target:
            if now<target:
                now+=j
                tmp.append(j)
                j+=1
            elif now>target:
                now-=i
                tmp.pop(0)
                i+=1
            else:
                res.append(tmp.copy())
                now-=i
                tmp.pop(0)
                i+=1
        return res

a = Solution()
target = 9
target = 15
res = a.findContinuousSequence(target)
print(res)


