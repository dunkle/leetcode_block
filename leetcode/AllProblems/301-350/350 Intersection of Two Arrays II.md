讲两个数组排序，然后从小比较大小，每次选取小的加入到最终结果中。

~~~python
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        result = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i, j = i+1, j+1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return result
~~~

