class Solution:
    def reOrderArray(self, array):
        # write code here
        n = len(array)-1
        if n<2:
            return array
        flag =0
        while flag<=n:
            if not array[n]&1:
                n-=1
                continue
            temp = array[n]
            j = n
            while j>0:
                array[j] = array[j-1]
                j-=1
            array[0] = temp
            flag += 1
        return array

a = Solution()
array = [1,2,3,4,5,6,7]
results = a.reOrderArray(array)
print(results)