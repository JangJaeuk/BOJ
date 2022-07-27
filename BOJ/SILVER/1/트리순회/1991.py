# 트리 순회 문제 무난

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def preorder(v):
    print(chr(v+65), end='')
    if tree[v][0] != '.':
        preorder(ord(tree[v][0])-65)
    if tree[v][1] != '.':
        preorder(ord(tree[v][1])-65) 
        
def inorder(v):
    if tree[v][0] != '.':
        inorder(ord(tree[v][0])-65)
    print(chr(v+65), end='')
    if tree[v][1] != '.':
        inorder(ord(tree[v][1])-65) 
        
def postorder(v):
    if tree[v][0] != '.':
        postorder(ord(tree[v][0])-65)
    if tree[v][1] != '.':
        postorder(ord(tree[v][1])-65)
    print(chr(v+65), end='')

if __name__ == "__main__":
    n = int(input())
    tree = [[] for _ in range(n)]
    for _ in range(n):
        sv, lc, rc = input().split()
        tree[ord(sv)-65] = (lc, rc)
    preorder(0)
    print()
    inorder(0)
    print()
    postorder(0)
    print()