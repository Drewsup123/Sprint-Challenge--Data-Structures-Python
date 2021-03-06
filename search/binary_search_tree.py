class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def enqueue(self, item):
        self.storage.add_to_tail(item)

    def dequeue(self):
        if self.storage.head is None:
            return None
        else:
            old_head = self.storage.head.value
            self.storage.remove_head()
            return old_head

    def len(self):
        head = self.storage.head
        if head is None:
            return 0
        elif head.get_next() is None:
            return 1
        else:
            count = 1
            while head.get_next() is not None:
                count += 1
                head = head.get_next()
            return count


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_index = Node(value)
        if self.tail is not None:
            self.tail.set_next(new_index)
        else:
            self.head = new_index
        self.tail = new_index

    def remove_head(self):
        # self.head = None
        if self.head is not None:
            new = self.head.next_node
            val = self.head.get_value()
            del self.head
            self.head = new
            if self.head is None:
                del self.tail
                self.tail = None
            return val

    def contains(self, value):
        current = self.head
        while 1:
            if current is None:
                return False
            elif current.value == value:
                return True
            else:
                current = current.next_node

    def get_max(self):
        if self.head is None:
            return None
        max_val = self.head.get_value()
        current = self.head
        while current is not None:
            if current.get_value() > max_val:
                max_val = current.get_value()
            current = current.get_next()
        return max_val


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def depth_first_for_each(self, cb):
        if self.value is not None:
            # Running function on initial value
            cb(self.value)
            if self.left is not None:
                self.left.depth_first_for_each(cb)
            if self.right is not None:
                self.right.depth_first_for_each(cb)
        else:
            pass

    def breadth_first_for_each(self, cb):
        # start from the bottom of the tree
            #How do we start from the bottom of the tree?
        # traverse our way upward calling cb on each node
        # return that array / change current array
        queue = Queue()
        queue.enqueue(self)
        while queue.storage.head:
            node = queue.storage.head.value
            node.value = cb(node.value)
            if node.left is not None:
                queue.enqueue(node.left)
            if node.right is not None:
                queue.enqueue(node.right)
            queue.dequeue()

    def copy_tree(self, copied=[]):
        if self.value is not None:
            copied.append(self.value)
            if self.left is not None:
                self.left.copy_tree(copied)
            if self.right is not None:
                self.right.copy_tree(copied)
        return copied

    def insert(self, value):
        new_tree = BinarySearchTree(value)
        if value < self.value:
            if not self.left:
                self.left = new_tree
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = new_tree
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        if self.left:
            if self.left.contains(target):
                return True
        if self.right:
            if self.right.contains(target):
                return True
        return False

    def get_max(self):
        if not self:
            return None
        max_value = self.value
        current = self
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.right
        return max_value
