 def depth_first(self, node):
        depth_first = []
        stack = [node]
        depth_first.append(node.value)

        while stack:
            edges = self._adjacency_list[stack[len(stack)-1]]
            stack.pop()
            for edge in edges:
                children = edge.node.value
                if children not in depth_first:
                    depth_first.append(children)
                    stack.append(edge.node)

        return depth_first