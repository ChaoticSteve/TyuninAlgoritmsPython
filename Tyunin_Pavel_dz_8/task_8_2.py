'''
Закодируйте любую строку из трех слов по алгоритму Хаффмана.
'''

from collections import Counter, deque


class Node:

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def haffman_tree(s):
    count_s = Counter(s)

    sorted_s = deque(sorted(count_s.items(), key=lambda item: item[1]))

    while len(sorted_s) > 1:

        weight = sorted_s[0][1] + sorted_s[1][1]
        node = Node(left=sorted_s.popleft()[0], right=sorted_s.popleft()[0])

        for i, item in enumerate(sorted_s):
            if weight > item[1]:
                continue
            else:
                sorted_s.insert(i, (node, weight))
                break
        else:
            sorted_s.append((node, weight))

    return sorted_s[0][0]


code_table = dict()


def haffman_code(tree, path=''):
    if not isinstance(tree, Node):
        code_table[tree] = path

    else:
        haffman_code(tree.left, path=f'{path}0')
        haffman_code(tree.right, path=f'{path}1')


some_string = 'first second third'
haffman_code(haffman_tree(some_string))

for i in some_string:
    print(i + ':', code_table[i], end=' ')
