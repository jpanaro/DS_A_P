class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

visible_nodes = 0
        
def visible_tree_node(root: Node) -> int:
    
    # First call is always on root so parent value is "zero"
    dfs(root, float('-inf'))
    
    return visible_nodes

def dfs(root: Node, value: int):
    global visible_nodes
    
    # Process current Node
    if root is None:
        return 0
    elif root.val >= value:
        visible_nodes += 1
        value = root.val
        
    # Process left node
    left = dfs(root.left, value)
    # Process right node
    right = dfs(root.right, value)
    
    return 0

# this function build a tree from input
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = visible_tree_node(root)
    print(res)
