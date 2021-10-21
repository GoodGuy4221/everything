from binarytree import tree, bst, Node

wood = tree(height=3, is_perfect=True)
# print(wood)
find_wood = bst(height=3, is_perfect=True)


# print(find_wood)


class MyNode:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.value} => {self.left} - {self.right}'


instance = MyNode(52)
instance.left = MyNode(12)
instance.right = MyNode('lorem')
instance.left.right = MyNode(23)
print(instance)

instance_node = Node(52)
instance_node.left = Node(12)
instance_node.right = Node(3)
instance_node.left.right = Node(23)
# print(instance_node)

binary_wood = bst(height=6, is_perfect=True)
print(binary_wood)

num = int(input('Enter number '))


def go(bin_tree, number, path='') -> str:
    if number == bin_tree.value:
        return f'Number found on the way:\nRooT{path}'
    if number < bin_tree.value and bin_tree.left is not None:
        return go(bin_tree.left, number, path=f'{path}\nStep Left')
    if number > bin_tree.value and bin_tree.right is not None:
        return go(bin_tree.right, number, path=f'{path}\nStep Right')
    return f'Number {number} is missing'


print(go(binary_wood, num))
