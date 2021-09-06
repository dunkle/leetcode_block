'''
result=[]
def backtrack(路径，选择列表):
    if 满足结束条件：
        result.append(路径)
        return
    for 选择 in 选择列表：
        做出选择
        递归执行backtrack
        撤销选择

时间复杂度：O(N*N!)。
空间复杂度：O(N)
作者：jue-qiang-zha-zha
链接：https://leetcode-cn.com/problems/n-queens/solution/51-n-huang-hou-hui-su-suan-fa-by-jue-qia-gh95/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''