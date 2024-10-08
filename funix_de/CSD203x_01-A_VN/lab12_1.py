import sys

def reach(adj, x, y):
  #write your code here
  # Perform a depth-first search to check if there is a path between `x` and `y`
  def explore(vertex):
    visited[vertex]=True #mark the current vertex as visited
    for neightbor in adj[vertex]:
      if not visited[neightbor]:
        explore(neightbor) #recursive explore neightbor if not yet visited
  visited=[False]*len(adj)
  explore(x) # start explore from vertex 'x'
  return int(visited[y]) # return 1 if vertex 'y' is visited, 0 otherwise

if __name__ == '__main__':
  input = sys.stdin.read()
  data = list(map(int, input.split()))
  n, m = data[0:2]
  data = data[2:]
  edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
  x, y = data[2 * m:]
  adj = [[] for _ in range(n)]
  x, y = x - 1, y - 1
  for (a, b) in edges:
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)
  print(reach(adj, x, y))