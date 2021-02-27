class Node:
    def __init__(self, value = None) -> None:
        self.value = value
        self.next = None
    

class Solution:
    def addTwoNumbersRecursive(self, l1, l2, remaining) -> int:
        tmp = remaining

        if not l1 and not l2 and remaining == 0:
            return None

        if l1 != None:
            tmp += l1.value
        else:
            l1 = Node(0)
        if l2 != None:
            tmp += l2.value
        else:
            l2 = Node(0)
        
        if tmp >=10:
            remaining = 1
            res = Node(tmp - 10)
        else:
            remaining = 0
            res = Node(tmp)

        res.next = self.addTwoNumbersRecursive(l1.next, l2.next, remaining)

        return res

    def addTwoNumbersIterative(self, l1, l2) -> Node:
        remaining = 0
        haveFirstElement = False
        while l1 != None or l2 != None:
            res = remaining
            if l1 != None:
                res += l1.value
                l1 = l1.next
            if l2 != None:

                res += l2.value
                l2 = l2.next
            if res >= 10:
                remaining = 1
            else:
                remaining = 0

            if not haveFirstElement:
                print('hello')
                ret = Node(res % 10)
                firstNode = ret
                haveFirstElement = True
                continue

            ret.next = Node(res % 10)
            ret = ret.next

        return firstNode


    def addTwoNumbers(self, l1, l2) -> int:
        return self.addTwoNumbersIterative(l1, l2)
    



# 21342
node1 = Node(2)
node1.next = (Node(4))
node1.next.next = (Node(3))
node1.next.next.next = (Node(1))
node1.next.next.next.next = (Node(2))


# 465
node2 = Node(5)
node2.next = (Node(6))
node2.next.next = (Node(4))

res = Solution().addTwoNumbers(node1, node2)

# print("result = {}".format(res.value))

while res:
    print(res.value, end='->')
    res = res.next

