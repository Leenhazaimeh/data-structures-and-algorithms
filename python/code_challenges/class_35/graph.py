class Vertex:
  pass

class Edge:
  def __init__(self, vertex, weight=1):
    pass

# edge1 = Edge(vertex)

class Graph:
  def __init__(self):
    self._adjacency_list = {
      # node: [edge1, edge2]
    }
  
  def add_vertex(self, vertex: Vertex):
    """ 
    Adds a vertex to the graph

    arguments
    vertex: Vertex


    """
    pass

  def add_edges(self, vertex1, vertex2, weight=1):
    """ 
    Adds an edge to our graph
    
    """  
    pass
  
  def get_nodes(self):
    pass

  def get_neighbors(self):
    pass
  
  def to_adj_list(self):
    return self._adajacency_list
  
  def _breadthFirst(self, action=lambda x: print(x)):
    """ 
    Performs a level order traversal of the graph and calls action at each node
    """

    # ALGORITHM BreadthFirst(vertex)
    # DECLARE nodes <-- new List()
    # DECLARE breadth <-- new Queue()
    # DECLARE visited <-- new Set()

    # breadth.Enqueue(vertex)
    # visited.Add(vertex)

    # while (breadth is not empty)
    #     DECLARE front <-- breadth.Dequeue()
    #     nodes.Add(front) # call action here

    #     for each child in front.Children
    #         if(child is not visited)
    #             visited.Add(child)
    #             breadth.Enqueue(child)   

    # return nodes;
    pass

  def _depthFirst(self, action=lambda x: print(x)):
    """ 
    Performs a depth first travesal of the graph and calls action at each node
    """
    pass