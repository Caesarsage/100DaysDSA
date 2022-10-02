class Solution:
  def clone_graph(node):
    oldToNewhMap = {}

    def dfs(node):
      if node in oldToNewhMap:
        return oldToNewhMap[node]

      newGraph = Node(node.val)
      oldToNewhMap[node] = newGraph

      for neighbor in node.neighbor:
        curr = dfs(neighbor)
        newGraph.neighbor.append(curr)
      return newGraph