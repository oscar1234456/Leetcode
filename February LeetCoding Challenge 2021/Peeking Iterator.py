# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.d = deque()
        while iterator.hasNext():
            self.d.append(iterator.next())
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.d[0] 
#     if len(self.d) != 0 else None
        

    def next(self):
        """
        :rtype: int
        """
        return self.d.popleft()

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.d)!=0
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].


#Solution 2:
# class PeekingIterator:
    # def __init__(self, iterator):
    #     """
    #     Initialize your data structure here.
    #     :type iterator: Iterator
    #     """
    #     self.pk = None
    #     self.iter = iterator
    #     if self.iter.hasNext():
    #         self.pk = self.iter.next()
        
        
    # def peek(self):
    #     """
    #     Returns the next element in the iteration without advancing the iterator.
    #     :rtype: int
    #     """
    #     return self.pk

    # def next(self):
    #     """
    #     :rtype: int
    #     """
    #     temp = self.pk
    #     if self.iter.hasNext():
    #         self.pk = self.iter.next()
    #     else:
    #         self.pk = None
    #     return temp
        

    # def hasNext(self):
    #     """
    #     :rtype: bool
    #     """
    #     return self.pk is not None