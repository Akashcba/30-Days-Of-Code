# Linked Lists in Python
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
'''   ## Hackerrank Backend Code
    def insert(self,head,data):
    #Complete this method
        if head == None:
            temp = Node(data)
            head = temp
        else:
            temp = head
            while(temp.next!=None):
                temp = temp.next
            temp2 = Node(data)
            temp.next = temp2
        return head

'''
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
mylist.display(head);
'''
