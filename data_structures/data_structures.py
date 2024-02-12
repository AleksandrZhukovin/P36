class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def add(self, value, element=None):
        if not self.head:
            self.head = Node(value)
            self.length += 1
        else:
            if not element.next:
                element.next = Node(value)
                self.length += 1
                return element
            return self.add(value=value, element=element.next)

    def get(self, target, element, current=0):
        if not element:
            return None
        elif target + 1 > self.length:
            return None
        else:
            if target == current:
                return element
            return self.get(target, element.next, current + 1)


class Stack(LinkedList):
    def remove(self, element=None):  # pop
        if self.length == 0:
            return None
        elif self.length == 1:
            a = self.head
            self.head = None
            return a
        elif self.length == 2:
            a = self.head.next
            self.head.next = None
            return a
        else:
            if not element.next.next:
                a = element.next
                element.next = None
                return a
            return self.remove(element.next)

    def delete(self, element):  # remove
        if not self.head:
            return None
        else:
            if not element.next:
                del element
            return self.delete(element.next)


class Que(LinkedList):
    def remove(self):
        if not self.head:
            return None
        else:
            a = self.head
            if self.head.next:
                self.head = self.head.next
            else:
                self.head = None
            return a


class BinaryTree:
    def __init__(self):
        self.head = None

    def add(self, value, direction, element=None):
        if not self.head:
            self.head = BinaryNode(value)
            return 1
        else:
            if direction == 'r':
                if not element.right:
                    element.right = BinaryNode(value)
                    return 1
                return self.add(value, direction, element.right)
            if direction == 'l':
                if not element.left:
                    element.left = BinaryNode(value)
                    return 1
                return self.add(value, direction, element.left)

    def delete(self, value, direction, element=None):
        if not self.head:
            return None
        else:
            if direction == 'r':
                if not element.right:
                    del element.right
                    return 1
                return self.add(value, direction, element.right)
            if direction == 'l':
                if not element.left:
                    del element.left
                return self.add(value, direction, element.left)


ll = LinkedList()

ll.add(1, ll.head)
ll.add(2, ll.head)
ll.add(3, ll.head)
ll.add(4, ll.head)


class GraphNode:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class Graph:
    def __init__(self, nodes=None):
        self.nodes = nodes
        self.connection_matrix = [[0] * len(nodes) for _ in range(len(nodes))]

    def connect(self, node1, node2):
        node1_index = self.nodes.index(node1)
        node2_index = self.nodes.index(node2)
        self.connection_matrix[node1_index][node2_index] = 1
        self.connection_matrix[node2_index][node1_index] = 1

    def disconnect(self, node1, node2):
        node1_index = self.nodes.index(node1)
        node2_index = self.nodes.index(node2)
        self.connection_matrix[node1_index][node2_index] = 0
        self.connection_matrix[node2_index][node1_index] = 0

    def add_node(self, value):
        self.nodes.append(GraphNode(value))
        self.connection_matrix = [i.append(0) for i in self.connection_matrix]
        self.connection_matrix.append([0] * len(self.nodes))

    def visualize(self):
        for i in self.nodes:
            print(i, end=' ')
        print('\n')
        n = 0
        for i in self.connection_matrix:
            print(self.nodes[n], i)
            n += 1


a = GraphNode('A')
b = GraphNode('B')
c = GraphNode('C')
d = GraphNode('D')
e = GraphNode('E')

g = Graph([a, b, c, d, e])

g.visualize()


