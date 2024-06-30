class ll:
    def __init__(self,data):
        self.data=data
        self.next=None
def printl(head):
    cur=head
    while cur!=None:
        print(cur.data,end="--->")
        cur=cur.next
    print()
def insert_head(head,val):
    newNode=ll(val)
    if head==None:
        return newNode
    newNode.next=head
    return newNode
def insert_tail(head,val):
    newNode=ll(val)
    if head==None:
        return newNode
    tail=head
    while tail.next!=None:
        tail=tail.next
    tail.next=newNode
    return head

o=ll(100)
o1=ll(300)
o.next=o1
head=insert_head(o,50)
printl(head)
head=insert_tail(head,350)
printl(head)
