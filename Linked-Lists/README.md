Linked-Lists — boxes(class node:) — hold element(data) — boxes point to the next box(self.next = None )

class node:
    def __init__(self, data):
        self.data = data  # The data itself
        self.next = None  

head = node("linked_lists")
head.next = node("sql_basics")
