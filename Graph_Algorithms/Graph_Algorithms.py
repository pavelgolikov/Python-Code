"""Graph questions"""

from Data_Structures.Disjoint_Set_Union_Rank_Path_Comp import makeset, find, union, combine_dsets
from Data_Structures.Stack import Stack
from copy import copy, deepcopy
import sys
inf = sys.maxsize


"""Graph questions"""

# def bfs(gnode: GNode) -> None:
#     """Breadth first traversal of self using queue."""
#
#     q = Queue()
#     lst = []
#     q.add(gnode)
#     lst.append(gnode)
#
#     while not q.is_empty():
#         el = q.remove()  # remove element from queue
#         print(el.value)
#         for node in el.adj_list:
#             # if the node is not in the list,
#             # add it to the list and to the queue
#             if node not in lst:
#                 lst.append(node)
#                 q.add(node)
#
#
# def dfs(gnode: GNode) -> None:
#     """Breadth first traversal of self using queue."""
#
#     s = Stack()
#     lst = []
#     s.add(gnode)
#     lst.append(gnode)
#
#     while not s.is_empty():
#         el = s.remove()  # remove element from stack
#         print(el.value)
#         for node in el.adj_list:
#             # if the node is not in the list,
#             # add it to the list and to the stack
#             if node not in lst:
#                 lst.append(node)
#                 s.add(node)


class GraphUndirNoWeight:
    """Graph.
    """
    def __init__(self) -> None:
        """Create an instance of GNode"""
        self.vertices = []
        self.edges = []
        self.adj_dict = {}

    def add_edge(self, u, v):
        """Add edge (u,v) to graph self."""
        if u not in self.vertices:
            self.vertices.append(u)
        if v not in self.vertices:
            self.vertices.append(v)
        if u in self.adj_dict.keys():
            self.adj_dict[u].append(v)
        else:
            self.adj_dict[u] = [v]
        if v in self.adj_dict.keys():
            self.adj_dict[v].append(u)
        else:
            self.adj_dict[v] = [u]


def connected_components(g: GraphUndirNoWeight)-> dict:
    """Return the dictionary with connected components of Graph g.
    """
    sets = {}
    for el in g.vertices:
        sets[el] = makeset(el)
    for ed in g.edges:
        if find(sets[ed[0]]) != find(sets[ed[1]]):
            union(sets[ed[0]], sets[ed[1]])
    return sets


def print_connected_components(d: dict):
    """Print connected components from dictionary."""
    lst = []
    for el in d.values():
        lst.append(el)
    return combine_dsets(lst)


def cycle_detection(g: GraphUndirNoWeight) -> bool:
    """Returns true if graph contains cycle, returns False otherwise."""
    sets = {}
    for el in g.vertices:
        sets[el] = makeset(el)
    for ed in g.edges:
        if find(sets[ed[0]]) != find(sets[ed[1]]):
            union(sets[ed[0]], sets[ed[1]])
        else:
            return True
    return False


def mst_kruskal(g: GraphUndirNoWeight)-> list:
    """Return a list containint mst of g using Kruskal's algorithm.
    """
    # lst is a list of endges that for mst
    lst = []
    # sets - disjoint sets formed using vertices
    sets = {}
    for el in g.vertices:
        sets[el] = makeset(el)
    # sort edges in ascending order
    sorted_ = sorted(g.edges, key=lambda tup: tup[2])
    for ed in sorted_:
        if find(sets[ed[0]]) != find(sets[ed[1]]):
            union(sets[ed[0]], sets[ed[1]])
            lst.append(ed)
    return lst


def mst_penn(g: GraphUndirNoWeight, start) -> list:
    """Return a list containint mst of g using Penn's algorithm. Start
    is the starting vertex.
    """
    # create mst_set
    mst_set = []
    # assign key values to all vertices in the graph, originally None
    keys = {}
    for el in g.vertices:
        if el == start:
            keys[el] = 0
        else:
            keys[el] = 999

    while keys:
        # pick vertex from keys with minimum value
        min_value_vertex = min(keys, key=keys.get)
        # include min_value_vertex into mst_set
        mst_set.append((min_value_vertex, keys[min_value_vertex]))
        # remove min_value_vertex from keys
        del keys[min_value_vertex]
        # update keys
        for ed in g.edges:
            if ed[0] == min_value_vertex and ed[1] in keys.keys():
                if ed[2] < keys[ed[1]]:
                    keys[ed[1]] = ed[2]
            elif ed[1] == min_value_vertex and ed[0] in keys.keys():
                if ed[2] < keys[ed[0]]:
                    keys[ed[0]] = ed[2]
    return mst_set


def dijikstra(g: GraphUndirNoWeight, source) -> list:
    """Return a list containint shortest path from source to every other node
     of g using Dijkstra's algorithm.
    Source is the starting vertex.
    """
    # create spt_set
    spt_set = []
    # create a list of vertices that have not been visited
    distances = {}
    for el in g.vertices:
        if el == source:
            distances[el] = 0
        else:
            distances[el] = 999
    distances_queue = copy(distances)

    while distances_queue:
        # pick vertex from keys with minimum value that is not in spt_set
        min_value_vertex = min(distances_queue, key=distances_queue.get)
        # include min_value_vertex into spt_set
        spt_set.append((min_value_vertex, distances[min_value_vertex]))
        # remove min_value_vertex from not_visited list
        # update keys
        for ed in g.edges:
            # for each adjecent node u
            if ed[0] == min_value_vertex and ed[1] in distances.keys():
                # u = ed[1], v = ed[0], weight(u,v) = ed[2]
                if ed[2] + distances[ed[0]] < distances[ed[1]]:
                    distances[ed[1]] = ed[2] + distances[ed[0]]
                    distances_queue[ed[1]] = ed[2] + distances_queue[ed[0]]
            elif ed[1] == min_value_vertex and ed[0] in distances.keys():
                # u = ed[0], v = ed[1], weight(u,v) = ed[2]
                if ed[2] + distances[ed[1]] < distances[ed[0]]:
                    distances[ed[0]] = ed[2] + distances[ed[1]]
                    distances_queue[ed[0]] = ed[2] + distances_queue[ed[1]]
        del distances_queue[min_value_vertex]
    return spt_set


def artic_point(gr: GraphUndirNoWeight):
    """Find all articulation points of graph g."""

    # create visited, low, and disc dictionaries:
    visited_ = {}
    disc_ = {}
    low_ = {}
    parent_ = {}
    for el in gr.vertices:
        visited_[el] = False
        disc_[el] = inf
        low_[el] = inf
        parent_[el] = None

    def artic_detect(g: GraphUndirNoWeight, parent: dict,
                     visited: dict, disc: dict, low: dict, ver, time_):
        """Helper function that actually looks for articulation points"""
        visited[ver] = True
        disc[ver] = time_
        low[ver] = disc[ver]
        child = 0
        # print(ver, time_, disc[ver], low[ver])
        for v in g.adj_dict[ver]:
            if visited[v] is False:
                # look at all adjacent vertices
                parent[v] = ver
                child += 1
                # perform artic_point on the child
                artic_detect(g, parent, visited, disc, low, v, time_+1)
                low[ver] = min(low[ver], low[v])
                # print(v, disc[v], low[v])
                if parent[ver] is None and child > 1:
                    print(ver)
                if parent[ver] is not None and low[v] >= disc[ver]:
                    print(ver)
            elif parent[ver] != v:
                low[ver] = min(low[ver], disc[v])

    artic_detect(gr, parent_, visited_, disc_, low_, 'a', 0)


g0 = GraphUndirNoWeight()
g0.add_edge('a', 'e')
g0.add_edge('a', 'b')
g0.add_edge('b', 'c')
g0.add_edge('c', 'd')
g0.add_edge('e', 'c')
artic_point(g0)


g0.vertices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k']
g0.edges = [('a', 'e', 1), ('e', 'g', 2), ('e', 'f', 23), ('f', 'k', 3),
            ('k', 'g', 4), ('g', 'j', 5), ('j', 'k', 6), ('k', 'h', 7),
            ('h', 'b', 8), ('c', 'b', 9), ('c', 'd', 10), ('a', 'd', 12),
            ('b', 'a', 14), ('e', 'h', 14), ('h', 'j', 18), ('a', 'g', 16)]


class DirGraph:
    """Directed Graph. Weighted."""

    def __init__(self):
        """Create instance of directed graph."""
        self.vertices = []
        self.adj_dict = {}
        self.adj_matrix = []

    def add_edge(self, u, v, weight):
        """Add edge (u,v) to graph self."""
        if u not in self.vertices:
            self.vertices.append(u)
        if v not in self.vertices:
            self.vertices.append(v)
        if u in self.adj_dict.keys():
            self.adj_dict[u].append((v, weight))
        else:
            self.adj_dict[u] = [(v, weight)]
        if v not in self.adj_dict.keys():
            self.adj_dict[v] = []


def dfs(g: DirGraph):
        """DFSearch of g."""
        def visit(g: DirGraph, visited, v):
            """Helper function."""
            print(v)
            visited[v] = 1
            for adj_vertex in g.adj_dict[v]:
                if visited[adj_vertex[0]] == 0:
                    visit(g, visited, adj_vertex[0])

        # create a visited dictionary
        visited = {el: 0 for el in g.adj_dict.keys()}
        for ver in g.vertices:
            if visited[ver] != 1:
                visit(g, visited, ver)


def topological_sort(g: DirGraph):
    """Topological sort of graph g."""

    def visit(g: DirGraph, visited, v, s: Stack):
        """Helper function."""
        visited[v] = 1
        for adj_vertex in g.adj_dict[v]:
            if visited[adj_vertex[0]] == 0:
                visit(g, visited, adj_vertex[0], s)
        s.add(v)

    # stack to keep track of which nodes comes before which
    s = Stack()
    # dictionary of nodes already visited
    visited = {el: 0 for el in g.adj_dict.keys()}
    # run through vertices and visit every one that is not yet visited
    for ver in g.vertices:
        if visited[ver] == 0:
            visit(g, visited, ver, s)
    # print all vertices
    while not s.is_empty():
        print(s.remove())


def floyd_warshall(g: DirGraph) -> list:
    """Return a list of shortest minimum distances between nodes of g
    using Floyd_Warshall algorithm."""

    # initialize solution matrix as g's adhacency matrix
    sol_matrix = deepcopy(g.adj_matrix)

    # 0 = a, 1 = b,
    for k in range(7):
        for i in range(7):
            for j in range(7):
                # if distance i->k + k->j is smaller than i->j
                if sol_matrix[i][k] + sol_matrix[k][j] < sol_matrix[i][j]:
                    sol_matrix[i][j] = sol_matrix[i][k] + sol_matrix[k][j]
    return sol_matrix


def boggle_(matrix: list, dictionary_: list):
    """Print words from the dictionary that can be formed with
    letters from input matrix."""

    def boggle(matrix: list, dictionary_: list, w: str, row, col):
        """Helper function to consider all combinations."""
        # get the letter from matrix
        # print(row, col)
        letter = matrix[row][col]
        # mark letter as visited
        matrix[row][col] = '-'
        # construct new word
        word = w + letter
        # print(word)
        if word in dictionary_:
            print(word)
        # call boggle with word as argument on all adjecent cells
        for i in range(-1, 2):
            if i + row > len(matrix)-1 or i + row < 0:
                continue
            for j in range(-1, 2):
                if j + col > len(matrix)-1 or j + col < 0:
                    continue
                # print(i + row, j + col)
                if matrix[i + row][j + col] == '-':
                    continue
                boggle(matrix, dictionary_, word, i + row, j + col)

        # unmark letter as visited
        matrix[row][col] = letter

    # start the possible string from every character:
    for i_ in range(len(matrix)):
        for j_ in range(len(matrix)):
            boggle(matrix, dictionary_, '', i_, j_)


# g = DirGraph()
# g.add_edge('a', 'b', 8)
# g.add_edge('a', 'c', 1)
# g.add_edge('b', 'd', 5)
# g.add_edge('b', 'k', 5)
# g.add_edge('f', 'd', 6)
# g.add_edge('a', 'f', 3)
# g.add_edge('b', 'f', 1)
# g.add_edge('c', 'e', 2)
# g.add_edge('e', 'g', 4)
# g.add_edge('g', 'f', 7)
# g.add_edge('e', 'f', 6)
# g.add_edge('g', 'd', 20)
# g.add_edge('k', 'd', 16)
# g.adj_matrix = [[0, 8, 1, inf, inf, 3, inf],
#                 [inf, 0, inf, 5, inf, 1, inf],
#                 [inf, inf, 0, inf, 2, inf, inf],
#                 [inf, inf, inf, 0, inf, inf, inf],
#                 [inf, inf, inf, inf, 0, 16, 4],
#                 [inf, inf, inf, 6, inf, 0, inf],
#                 [inf, inf, inf, 20, inf, 7, 0]]
# g.adj_matrix = [['g', 'i', 'z'],
#                 ['u', 'e', 'k'],
#                 ['q', 's', 'e']]
# dictionary_ = ['geeks', 'quiz']
# boggle_(g.adj_matrix, dictionary_)
