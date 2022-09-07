class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(tree: Node) -> bool:
    return dfs(tree) != -1

def dfs(root: Node) -> bool:
    if root is None:
        return 0
    
    left = dfs(root.left)
    if left == -1:
        return -1
    right = dfs(root.right)
    if right == -1:
        return -1
    
    if abs(left - right) > 1:
        return -1
    
    return max(left, right) + 1

# this function build a tree from input
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    tree = build_tree(iter(input().split()), int)
    res = is_balanced(tree)
    print('true' if res else 'false')
