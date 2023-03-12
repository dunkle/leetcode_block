# 384. Shuffle an Array

![image-20200408180153207](../../.assert/image-20200408180153207.png)

将数组随机打乱

## 暴力

每次从数组中随机选择一个值，直到所有都选完

~~~python
class Solution:
    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)

    def reset(self):
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self):
        aux = list(self.array)

        for idx in range(len(self.array)):
            remove_idx = random.randrange(len(aux))
            self.array[idx] = aux.pop(remove_idx)

        return self.array
~~~

## Fisher-Yates Algorithm

遍历数组，从后面随机选一个数与当前位置的数交换。

~~~python
class Solution:

    def __init__(self, nums: List[int]):
        self.array = nums
        self.origin = list(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.array = self.origin
        self.origin = list(self.origin)

        return self.origin
    
    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.array)):
            t = random.randrange(i, len(self.array))
            self.array[i], self.array[t] = self.array[t], self.array[i]
        return self.array
~~~

python中复制一个list可以直接对一个list变量调用list方法。

## 排序

对数组进行排序，排序的key是随机数。

~~~python
class Solution:

    def __init__(self, nums: List[int]):
        self.origin = list(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.origin
    
    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        return sorted(self.origin, key=lambda x: random.random())


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
~~~

