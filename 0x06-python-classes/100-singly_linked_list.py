#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        if type(data) is not int:
            raise TypeError("data must be an integer")
        elif next_node is not None and type(next_node) is not Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__data = data
            self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        node = Node(value)
        if self.__head is None:
            self.__head = node
        else:
            tmp = self.__head
            if node.data < tmp.data or \
                    (node.data == tmp.data and node.data < tmp.next_node.data):
                node.next_node = tmp
                self.__head = node
            else:
                prev = tmp
                while tmp is not None and tmp.data < value:
                    prev = tmp
                    tmp = tmp.next_node
                node.next_node = tmp
                prev.next_node = node

    def __str__(self):
        ch = ""
        tmp = self.__head
        while tmp is not None:
            ch += str(tmp.data)
            ch += "\n"
            tmp = tmp.next_node
        ch = ch[:-1]
        return ch
