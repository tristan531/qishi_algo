# -*- coding: utf-8 -*-
"""hw5 graphs.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ikh5sXkt-qc_6haN_4qJwXuqSRiMYgP9

1971. Find if Path Exists in Graph
"""

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def add_dict(d, k, v):
            if k in d:
                d[k].append(v)
            else:
                d[k] = [v]

        def buildG(edges):
            d = {}
            for e in edges:
                add_dict(d, e[0], e[1])
                add_dict(d, e[1], e[0])

            return d

        graph = buildG(edges)

        if n==1: return True
        if source not in graph or destination not in graph: return False

        from queue import Queue
        q = Queue()
        q.put(source)
        visited = set()
        visited.add(source)
        while q.qsize() > 0:
            cur = q.get()
            if destination in graph[cur]:
                return True
            else:
                visited.add(cur)
                for each in graph[cur]:
                    if each not in visited:
                        q.put(each)
        return False

"""997. Find the Town Judge

"""

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        # degree == n-1
        people = [0 for _ in range(n+1)]

        for i, j in trust:
            people[j] += 1
            people[i] -= 1

        for i in range(1, n+1):
            if people[i] == n-1: return i

        return -1

"""1129. Shortest Path with Alternating Colors

"""

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        def add(graph, edges, color):
            for i, j in edges:
                if i not in graph:
                    graph[i] = [(j, color)]
                else:
                    graph[i].append((j, color))

        graph = {}
        add(graph, redEdges, 0)
        add(graph, blueEdges, 1)

        res = [-1] * n

        from queue import Queue
        q= Queue()
        q.put((0, 0, 2)) # dist, node, color
        visited = set()
        dist = {}
        while q.qsize() > 0:

            curdist, curend, curcolor = q.get()
            if (curend, curcolor) in visited: continue
            visited.add((curend, curcolor))

            if curend not in dist: dist[curend] = curdist
            res[curend] = dist[curend]

            #res[curend] = curdist
            if curend not in graph: continue

            for node, color in graph[curend]:
                if color != curcolor:
                    q.put((curdist+1, node, color))

        return res

"""2359. Find Closest Node to Given Two Nodes

"""

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def getDist(node, d, edges, dist):
            # no outgoing edge, aka last node
            if node == -1: return

            if dist[node] == -1:
                dist[node] = d
                getDist(edges[node], d+1, edges, dist)

        distFromNode1 = [-1] * len(edges)
        distFromNode2 = [-1] * len(edges)
        getDist(node1, 0, edges, distFromNode1)
        getDist(node2, 0, edges, distFromNode2)
        print(distFromNode1)

        res = -1
        minDist = float('inf')
        for i in range(len(edges)):
            if min(distFromNode1[i], distFromNode2[i]) < 0:
                continue
            if max(distFromNode1[i], distFromNode2[i]) < minDist:
                minDist = max(distFromNode1[i], distFromNode2[i])
                res = i

        return res

"""2246. Longest Path With Different Adjacent Characters

"""

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        def dfs(root, graph, s):
            p1, p2 = 0, 0 # p1 >= p2
            if root not in graph: return 0

            for child in graph[root]:
                length = dfs(child, graph, s)
                length = 0 if s[child]==s[root] else length+1

                if length >= p1:
                    p2 = p1
                    p1 = length
                elif length >= p2:
                    p2 = length
            self.maxPath = max(self.maxPath, p1+p2)

            return p1

        graph = {}
        for i in range(1, len(parent)):
            if parent[i] in graph:
                graph[parent[i]].append(i)
            else:
                graph[parent[i]] = [i]

        self.maxPath = 0
        dfs(0, graph, s)
        return self.maxPath + 1