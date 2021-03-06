import bst

def height(node):
    if node is None:
        return -1
    else:
        return node.height


def update_height(node):
    node.height = max(height(node.left), height(node.right)) + 1


class AVL(bst.BST):
    def left_rotate(self, x):
        y = x.right
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.right = y.left
        if x.right is not None:
            x.right.parent = x
        y.left = x
        x.parent = y
        update_height(x)
        update_height(y)

    def right_rotate(self, x):
        y = x.left
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.left = y.right
        if x.left is not None:
            x.left.parent = x
        y.right = x
        x.parent = y
        update_height(x)
        update_height(y)

    def rebalance(self, node):
        while node is not None:
            update_height(node)
            if height(node.left) >= 2 + height(node.right):
                if height(node.left.left) >= height(node.left.right):
                    self.right_rotate(node)
                else:
                    self.left_rotate(node.left)
                    self.right_rotate(node)
            elif height(node.right) >= 2 + height(node.left):
                if height(node.right.right) >= height(node.right.left):
                    self.left_rotate(node)
                else:
                    self.right_rotate(node.right)
                    self.left_rotate(node)
            node = node.parent

    def insert(self, k):
        node = super(AVL, self).insert(k)
        self.rebalance(node)

    def insert_values(self, l):
        for v in l:
            self.insert(v)

    def delete(self, k):
        node = super(AVL, self).delete(k)
        self.rebalance(node.parent)

    def delete_values(self, l):
        for v in l:
            self.delete(v)

    def inorder_tree_walk(self):
        return super(AVL, self).inorder_tree_walk()

avl = AVL()
l = [3,4,5,7,9,10,13,1,-3,-2,-9]
avl.insert_values(l)
assert avl.inorder_tree_walk() == sorted(l)

to_delete = [3,4,5,-2]
avl.delete_values([3,4,5,-2])
for x in to_delete:
    l.remove(x)
assert avl.inorder_tree_walk() == sorted(l)
