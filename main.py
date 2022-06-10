from binarytree import build
from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None


def inorder(root_node):
    current = root_node
    if current is None:
        return
    inorder(current.left_child)
    print(current.data, end=" ")
    inorder(current.right_child)


def preorder(root_node):
    current = root_node
    if current is None:
        return
    print(current.data, end=" ")
    preorder(current.left_child)
    preorder(current.right_child)


def postorder(root_node):
    current = root_node
    if current is None:
        return
    postorder(current.left_child)
    postorder(current.right_child)
    print(current.data, end=" ")


def breadth_first_traversal(root_node):
    list_of_nodes = []
    traversal_queue = deque([root_node])

    while len(traversal_queue) > 0:
        node = traversal_queue.popleft()
        list_of_nodes.append(node.data)
        if node.left_child:
            traversal_queue.append(node.left_child)
        if node.right_child:
            traversal_queue.append(node.right_child)
    return list_of_nodes


n1 = Node('A')
n2 = Node('B')
n3 = Node('C')
n4 = Node('D')
n5 = Node('E')
n6 = Node('F')
n7 = Node('G')
n8 = Node('H')
n1.right_child = n3
n3.right_child = n6
n1.left_child = n2
n2.right_child = n5
n2.left_child = n4
n4.right_child = n8
n4.left_child = n7

a = build(['A', 'B', 'C', 'D', 'E', None, 'F', 'G', 'H'])
print(a)

print("preorder : ", end="")
preorder(n1)
print("\ninorder : ", end="")
inorder(n1)
print("\npostorder : ", end="")
postorder(n1)

print("\nbreadth_first_traversal ==", breadth_first_traversal(n1))
