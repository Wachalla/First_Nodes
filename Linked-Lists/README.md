Linked-Lists — boxes — hold element — boxes point to the next box

# Each box is a node
class node:
    def __init__(self, data):
        self.data = data  # The data itself
        self.next = None  # link to the next box

# first piece
head = node("linked_lists")
head.next = node("sql_basics")
