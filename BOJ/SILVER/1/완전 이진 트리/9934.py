import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def make_tree(inorder, depth):
    mid = len(inorder) // 2
    tree[depth].append(inorder[mid])
    if len(inorder) == 1:
        return
    make_tree(inorder[:mid], depth+1)
    make_tree(inorder[mid+1:], depth+1)


if __name__ == "__main__":
    k = int(input())
    inorder = list(map(int, input().split()))
    tree = [[] for _ in range(k)]
    make_tree(inorder, 0)
    for depth in tree:
        print(*depth)
