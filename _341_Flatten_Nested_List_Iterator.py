# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nlst = nestedList
        self.flst = []
        self.idx = 0

        def set_flst(lst):
            for itm in lst:
                if itm.isInteger():
                    self.flst.append(itm.getInteger())
                else:
                    set_flst(itm.getList())

        set_flst(self.nlst)

    def next(self):
        """
        :rtype: int
        """
        value = self.flst[self.idx]
        self.idx += 1
        return value

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.idx < len(self.flst)


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
