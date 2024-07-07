import math
import random

#A tree is represented by an array of integers.
#The ith index of this array gives the position
#of the red dot along the ith horizontal row in the tree.
#E.g., the following tree with depth 4
#                 r
#                / \
#               r   .
#              / \ / \
#             .   .   r
#            / \ / \ / \
#           .   .   .   r
#          / \ / \ / \ / \
#         .   .   r   .   .
#       
#would be represented as [0, 0, 2, 3, 2]

def genTrees(n):
    allTrees = []
    recTree(allTrees, [], 0, n)
    return allTrees

def recTree(allTrees, currTree, depth, n):
    if depth == n:
        allTrees.append(currTree)
        return
    for i in range(depth+1):
        copyCurrTree = currTree.copy()
        copyCurrTree.append(i)
        recTree(allTrees, copyCurrTree, depth + 1, n)

def genRandTree(n):
    tree = []
    for depth in range(n):
        tree.append(random.randint(0, depth))
    return tree

# A path is represented as just a sequence of ls and rs
# indicating whether from the root position of the tree you
# went left or right. E.g., the path [l, r, r, l] on the
# example tree above would go through the 1st, 2nd and 5th red dots.

def findPath(tree):
    allSuccessfulPaths = []
    allPaths = []
    recPath(0, 0, tree, 0, [], allSuccessfulPaths, allPaths)
    return allSuccessfulPaths, allPaths

def recPath(pos, depth, tree, n_red, currPath, allSuccPaths, allPaths):
    if depth == len(tree)-1:
        if tree[depth] == pos:
            n_red += 1
        val = math.floor(math.log2(len(tree))) + 1
        if n_red >= val:
            allSuccPaths.append( {'path': currPath.copy(), 'n_red': n_red} )
        else:
            allPaths.append(currPath.copy())
        return
    if tree[depth] == pos: #at red node
        leftPath = currPath.copy(); leftPath.append('l')
        rightPath = currPath.copy(); rightPath.append('r')
        recPath(pos, depth + 1, tree, n_red + 1, leftPath, allSuccPaths, allPaths)
        recPath(pos + 1, depth + 1, tree, n_red + 1, rightPath, allSuccPaths, allPaths)
    else:
        newPath = currPath.copy()
        newPath.append('l' if pos < tree[depth] else 'r') #move left if to the left of the red node at this layer
        recPath(pos + (1 if newPath[-1] == 'r' else 0), depth + 1, tree, n_red, newPath, allSuccPaths, allPaths)
    
def basicDraw(tree, depth, i, path = None):
    return u'\u24e1' if tree[depth] == i else '.'

def pathDraw(tree, depth, i, path):
    if i == path[depth]:
        return u'\u24c7' if i == tree[depth] else u'\u2b24'
    else:
        return u'\u24e1' if i == tree[depth] else '.'

def drawTree(tree, drawFn = basicDraw, path = None):
    n = len(tree); n_emptyspace =  ((3*(n-1) + n) // 2)
    output = ''
    for depth in range(len(tree)):
        output += ' ' * n_emptyspace
        for i in range(depth+1):
            output += drawFn(tree, depth, i, path)
            output += ' ' * 3
        output += '\n'
        n_emptyspace -= 1
        output += ' ' * n_emptyspace
        if depth < len(tree)-1:
            for i in range(depth+1):
                output += '/ \\ '
            output += '\n'
        n_emptyspace -= 1
    return output
    
def getNumericPath(path):
    numericPath = [0]
    pos = 0
    for i in range(len(path)):
        pos += 1 if path[i] == 'r' else 0
        numericPath.append(pos)
    return numericPath
        
        

if __name__ == '__main__':
#    randTree = genRandTree(800)
    randTree = [0, 0, 1, 1, 1, 1, 2, 2, 2, 6, 9, 9, 9, 0, 11, 5]
#    randTree = [0, 0, 2, 3, 2, 1, 0, 0, 2, 4, 6, 8, 10, 12, 14, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 30]
#    randTree = [0, 0, 2, 3, 2, 1, 0, 4]
    succPaths, remPaths = findPath(randTree)
    print('randomTree:', randTree)
    maxPath = max(succPaths, key = lambda x : x['n_red'])
    numPath = getNumericPath(maxPath['path'])
    print('best path:', maxPath['path'])
    print('n_red:', maxPath['n_red'])
    print(drawTree(randTree, pathDraw, numPath))
#    print('All other paths:')
#    for path in remPaths:
#        print(path)
#        numericPath = getNumericPath(path)
#        print(drawTree(randTree, pathDraw, numericPath))
    print('num successful paths:', len(succPaths))
    print('total number of paths:', len(remPaths) + len(succPaths))



'''
                              Ⓡ
                             / \
                            Ⓡ   .
                           / \ / \
                          .   Ⓡ   .
                         / \ / \ / \
                        .   Ⓡ   .   .
                       / \ / \ / \ / \
                      .   Ⓡ   .   .   .
                     / \ / \ / \ / \ / \
                    .   Ⓡ   .   .   .   .
                   / \ / \ / \ / \ / \ / \
                  .   .   Ⓡ   .   .   .   .
                 / \ / \ / \ / \ / \ / \ / \
                .   .   Ⓡ   .   .   .   .   .
               / \ / \ / \ / \ / \ / \ / \ / \
              .   .   Ⓡ   .   .   .   .   .   .
             / \ / \ / \ / \ / \ / \ / \ / \ / \
            .   .   ⬤   .   .   .   ⓡ   .   .   .
           / \ / \ / \ / \ / \ / \ / \ / \ / \ / \
          .   .   ⬤   .   .   .   .   .   .   ⓡ   .
         / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \
        .   .   ⬤   .   .   .   .   .   .   ⓡ   .   .
       / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \
      .   .   ⬤   .   .   .   .   .   .   ⓡ   .   .   .
     / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \
    ⓡ   .   ⬤   .   .   .   .   .   .   .   .   .   .   .
   / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \
  .   .   .   ⬤   .   .   .   .   .   .   .   ⓡ   .   .   .
 / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \
.   .   .   ⬤   .   ⓡ   .   .   .   .   .   .   .   .   .   .

'''
