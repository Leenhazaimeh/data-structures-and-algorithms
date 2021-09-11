# Graphs
 A graph needs to keep track of all the nodes in it, and all the edges that connect those nodes. We will also need a way to add nodes and edges to the graph in the first place. Minimally, this is enough to create a representation of a graph. However, for our API to be much use, we’ll want a few more features

## Challenge
Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:

    add node
        Arguments: value
        Returns: The added node
        Add a node to the graph
    add edge
        Arguments: 2 nodes to be connected by the edge, weight (optional)
        Returns: nothing
        Adds a new edge between two nodes in the graph
        If specified, assign a weight to the edge
        Both nodes should already be in the Graph
    get nodes
        Arguments: none
        Returns all of the nodes in the graph as a collection (set, list, or similar)
    get neighbors
        Arguments: node
        Returns a collection of edges connected to the given node
            Include the weight of the connection in the returned collection
    size
        Arguments: none
        Returns the total number of nodes in the graph

Structure and Testing

Utilize the Single-responsibility principle: any methods you write should be clean, reusable, abstract component parts to the whole challenge. You will be given feedback and marked down if you attempt to define a large, complex algorithm in one function definition.

Write tests to prove the following functionality:

    Node can be successfully added to the graph
    An edge can be successfully added to the graph
    A collection of all nodes can be properly retrieved from the graph
    All appropriate neighbors can be retrieved from the graph
    Neighbors are returned with the weight between nodes included
    The proper size is returned, representing the number of nodes in the graph
    A graph with only one node and edge can be properly returned
    An empty graph properly returns null


## Approach & Efficiency


    add_node :
        time : O(1)
        space : O(1)

    add_edge :
        time : O(n)
        space : O(n)

    get_nodes:
        time: O(n)
        space: O(n)

    get_neighbors:
        time: O(n)
        space: O(n)

    size:
        time: O(1)
        space: O(1)


## API


    add node: add node to the graph with value of the input and return the node.

    add edge: add edge between the two input nodes.

    get nodes: returns all of the nodes in the graph.

    get neighbors: return the edges and the weight to the input node.

    size: returns the total number of nodes in the graph.

