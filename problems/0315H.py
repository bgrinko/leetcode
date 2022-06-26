nums = [2, 5, 6, 1, 3, 3, 2, 0, -1, 7, 14, 2]


class Node:
    def __int__(self, l=None, r=None, v=None):
        self.v = v
        self.l = l
        self.r = r


lst = Node(v=nums[0])

for i in nums[1:]:
    if i >= lst.v:

