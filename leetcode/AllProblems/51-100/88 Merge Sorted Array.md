![image-20201008161047664](../../../.assert/image-20201008161047664.png)

给定两个有序数组，将nums2合并到nums1中，合并是inplace的操作。

利用nums2[0]，先在nums1中存前m个元素，交换到nums2时要对nums2进行排序，保证nums2[0]是最小的元素。

~~~python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums1) == 0:
            nums1 = nums2
        if len(nums2) == 0:
            return
        i, j = 0, 0
        while i < m:
            if nums1[i] <= nums2[0]:
                i += 1
            else:
                nums1[i], nums2[0] = nums2[0], nums1[i]
                nums2 = sorted(nums2)
        for j in range(n):
            nums1[i] = nums2[j]
            i, j = i+1, j+1
~~~

