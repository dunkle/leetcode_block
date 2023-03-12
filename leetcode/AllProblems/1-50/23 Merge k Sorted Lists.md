合并K个有序链表

## 暴力

将多个链表存放到数组中，排序，然后根据根据排序的数组构建链表

时间复杂度：

1. 收集所有节点时间复杂度为O(N)
2. 排序为O(NlogN)
3. 重建链表为O(N)

空间复杂度为O(N)

## 归并排序

两两合并。

~~~python
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        
        while len(lists) > 1:
            queue = []
            # 合并相邻的两个链表
            for i in range(0, len(lists), 2):
                if i == len(lists)-1:
                    queue.append(lists[i])
                else:
                    queue.append(self.merge2Lists(lists[i], lists[i+1]))
            lists = queue
        return lists[-1]
    
    
    def merge2Lists(self, list1, list2):
        head = p = ListNode(0)
        
        while list1 and list2:
            if list1.val > list2.val:
                p.next = list2
                list2 = list2.next
            else:
                p.next = list1
                list1 = list1.next
            p = p.next
            
        if list1:
            p.next = list1
        if list2:
            p.next = list2
            
        return head.next
~~~

时间复杂度为为O(Nlogk)，k为链表的数量。合并两个链表的时间为O(N)，则合并全部链表的时间为$O(\sum_{i=1}^{log2k})O(N)=O(Nlogk)$

空间复杂度为O(1)

## 有限队列

将所有队列放到堆中，每次取最小的值。

从堆中拿出一个值的时间复杂度为o(logk),共需拿出N个节点，因此时间复杂度为O(Nlogk)

