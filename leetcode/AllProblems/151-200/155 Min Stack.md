# 155. Min Stack

设计一个栈，能在常数时间内返回最小值。

![image-20200331123734314](../../.assert/image-20200331123734314.png)

设置一个常数，存储最小值，pop时注意当pop的是最小值时应该重新查找最小值。

~~~python
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []
        self.min = None
        

    def push(self, x: int) -> None:
        if self.min is None:
            self.min = x
        else:
            self.min = x if self.min > x else self.min
        self._stack.append(x)
        

    def pop(self) -> None:
        value = self._stack.pop()
        
        if len(self._stack) == 0:
            self.min = None
        elif value == self.min:
            self.min = min(self._stack)
        

    def top(self) -> int:
        if not self._stack:
            return None
        return self._stack[-1]

    def getMin(self) -> int:
        return self.min
~~~

这中方法在pop时查找最小值的时间是O(n),可以增加一个优先队列，让栈中的元素

~~~python
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []
        self.mins = []
        

    def push(self, x: int) -> None:
    	# 这里注意与最小值相等的情况也要push
    	# 只有比min[-1]小的元素才会进入mins，不会出现下面的情况：
    	# stack -2 -1 3 5
    	# mins -1 -2 3 5
    	# 因为-2不会比-1先进入mins
        if len(self.mins) == 0 or self.mins[-1] >= x:
            self.mins.append(x)
        self._stack.append(x)
        

    def pop(self) -> None:
        if self._stack is None:
            raise IndexError()
        if self.mins[-1] == self._stack.pop():
            self.mins.pop()
        

    def top(self) -> int:
        if not self._stack:
            raise IndexError()
        return self._stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]
~~~