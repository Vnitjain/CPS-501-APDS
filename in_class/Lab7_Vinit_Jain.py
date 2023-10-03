# Author: Vinit Kirit Jain
# Assignment: Lab 7
# Date: 2023-10-02

# Notes: Difference between stack and queue:
# stack follows LIFO (last element added is first removed)
# queue follows FIFO (first element added is first removed)
import collections

# Q1: Implement Stack with functions: .append, .pop. You can use python list, collections.deque, and queue.LifoQueu


class stack:
    # making a dequeue object in the constructor
    def __init__(self):
        self.stack_dequeue = collections.deque()

    # using the dequeue append function to add the element to the stack
    def append(self, element):
        self.stack_dequeue.append(element)

    # using the dequeue pop function to remove the element from the top
    def pop(self):
        popped_element = self.stack_dequeue.pop()
        return popped_element


# using the append and pop method to build a stack
stack_object = stack()
stack_object.append(30)
stack_object.append(30)
stack_object.append(30)
stack_object.append(20)
stack_object.pop()
# printing the final stack
print("Stack: " + str(stack_object.stack_dequeue))

# Q2: Implement Queue with functions .enqueue and .dequeue.
#    Enqueue adds element to the back while dequeue removes the first element


class queue:
    # using a list to store the elements of the queue
    def __init__(self):
        self.queue_list = []

    # using the append method of list to add element to the end
    def enqueue(self, element):
        self.queue_list.append(element)

    # removing the first element from the list by taking range from index 1 to the end
    def dequeue(self):
        self.queue_list = self.queue_list[1:]


# using the enqueue and dequeue methods to build queue
queue_object = queue()
queue_object.enqueue(10)
queue_object.enqueue(20)
queue_object.enqueue(30)
queue_object.enqueue(40)
queue_object.dequeue()
# printing the final queue
print(queue_object.queue_list)

# Q3: Implement Graph with functions add_node, add_edge, and print graph.
#    Print graph show for each node, every other node that shares an edge


class Graph:
    # using dictionary for storing the edges and list to store nodes
    def __init__(self):
        self.edge_list = {}
        self.node_list = []

    # using list append to add the node to the list
    def add_node(self, node):
        self.node_list.append(node)

    # if the vertex is present in the dictionary update it by appending the value to the list value else create new list for the vertex1
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.edge_list.keys():
            self.edge_list[vertex1].append(vertex2)
        else:
            self.edge_list[vertex1] = [vertex2]

    # printing all the nodes and edges of the graphs
    def print_graph(self):
        print("All the nodes: " + str(self.node_list))
        print("All the edges: " + str(self.edge_list))


# using add node and add edge methods to build a graph
graph_object = Graph()
graph_object.add_node(1)
graph_object.add_node(2)
graph_object.add_node(3)
graph_object.add_node(4)
graph_object.add_node(5)

graph_object.add_edge(1, 2)
graph_object.add_edge(1, 4)
graph_object.add_edge(1, 3)
graph_object.add_edge(2, 3)
graph_object.add_edge(2, 4)
graph_object.add_edge(2, 5)
graph_object.add_edge(4, 5)
graph_object.add_edge(4, 2)
graph_object.add_edge(5, 2)
graph_object.add_edge(5, 4)

# printing final graph
graph_object.print_graph()