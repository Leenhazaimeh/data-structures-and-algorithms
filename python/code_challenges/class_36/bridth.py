  
 class Vertex:

    def __init__(self,value):
        self.value = value

    def __str__(self):
        return f"{self.value}" 
  
  def breadth_first_search(self, start_vertex, action=(lambda x: None)):
        queue = Queue()
        visited = set()
        queue.enqueue(start_vertex)
        visited.add(start_vertex)