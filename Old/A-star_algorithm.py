class Node:
    """
    Represents a node in the grid. A node can be navigable
    (that is located in water)
    or it may belong to an obstacle (island).

    === Attributes: ===
    @type navigable: bool
       navigable is true if and only if this node represents a
       grid element located in the sea
       else navigable is false
    @type grid_x: int
       represents the x-coordinate (counted horizontally, left to right)
       of the node
    @type grid_y: int
       represents the y-coordinate (counted vertically, top to bottom)
       of the node
    @type parent: TNode
       represents the parent node of the current node in a path
       for example, consider the grid below:
        012345
       0..+T..
       1.++.++
       2..B..+
       the navigable nodes are indicated by dots (.)
       the obstacles (islands) are indicated by pluses (+)
       the boat (indicated by B) is in the node with
       x-coordinate 2 and y-coordinate 2
       the treasure (indicated by T) is in the node with
       x-coordinate 3 and y-coordinate 0
       the path from the boat to the treasure if composed of the sequence
       of nodes with coordinates:
       (2, 2), (3,1), (3, 0)
       the parent of (3, 0) is (3, 1)
       the parent of (3, 1) is (2, 2)
       the parent of (2, 2) is of course None
    @type in_path: bool
       True if and only if the node belongs to the path plotted by A-star
       path search
       in the example above, in_path is True for nodes with coordinates
       (2, 2), (3,1), (3, 0)
       and False for all other nodes
    @type gcost: float
       gcost of the node, as described in the handout
       initially, we set it to the largest possible float
    @type hcost: float
       hcost of the node, as described in the handout
       initially, we set it to the largest possible float
    """
    def __init__(self, navigable, grid_x, grid_y):
        """
        Initialize a new node

        @type self: Node
        @type navigable: bool
        @type grid_x: int
        @type grid_y: int
        @rtype: None

        Preconditions: grid_x, grid_y are non-negative

        >>> n = TNode(True, 2, 3)
        >>> n.grid_x
        2
        >>> n.grid_y
        3
        >>> n.navigable
        True
        """
        self.navigable = navigable
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.in_path = False
        self.parent = None
        self.gcost = sys.float_info.max
        self.hcost = sys.float_info.max

    def set_gcost(self, gcost):
        """
        Set gcost to a given value

        @type gcost: float
        @rtype: None

        Precondition: gcost is non-negative

        >>> n = TNode(True, 1, 2)
        >>> n.set_gcost(12.0)
        >>> n.gcost
        12.0
        """
        self.gcost = gcost

    def set_hcost(self, hcost):
        """
        Set hcost to a given value

        @type hcost: float
        @rtype: None

        Precondition: gcost is non-negative

        >>> n = TNode(True, 1, 2)
        >>> n.set_hcost(12.0)
        >>> n.hcost
        12.0
        """
        self.hcost = hcost

    def fcost(self):
        """
        Compute the fcost of this node according to the handout

        @type self: Node
        @rtype: float
        """
        return self.gcost + self.hcost

    def set_parent(self, parent):
        """
        Set the parent to self
        @type self: Node
        @type parent: Node
        @rtype: None
        """
        self.parent = parent

    def distance(self, other):
        """
        Compute the distance from self to other
        @self: TNode
        @other: TNode
        @rtype: int
        """
        dstx = abs(self.grid_x - other.grid_x)
        dsty = abs(self.grid_y - other.grid_y)
        if dstx > dsty:
            return 14 * dsty + 10 * (dstx - dsty)
        return 14 * dstx + 10 * (dsty - dstx)

    def __eq__(self, other):
        """
        Return True if self equals other, and false otherwise.

        @type self: Node
        @type other: Node
        @rtype: bool
        """
#        # TODO
#        flag = True
#
        if self.grid_x == other.grid_x and self.grid_y == other.grid_y:
            return True
        else:
            return False

    def __lt__(self, other):
        """
        Return True if self less than other, and false otherwise.

        @type self: Node
        @type other: Node
        @rtype: bool
        """

        return self.fcost() < other.fcost()



    def __str__(self):
        """
        Return a string representation.

        @type self: Node
        @rtype: str
        """
        # TODO
        if self.navigable == True:
            if self.in_path == True:
                return ('*')
            else:
                return ('.')
        else:
            return ('+')


def less_than(a,b):
        return a.fcost() < b.fcost()

class Grid:
    """
    Represents the world where the action of the game takes place.
    You may define helper methods as you see fit.

    === Attributes: ===
    @type width: int
       represents the width of the game map in characters
       the x-coordinate runs along width
       the leftmost node has x-coordinate zero
    @type height: int
       represents the height of the game map in lines
       the y-coordinate runs along height; the topmost
       line contains nodes with y-coordinate 0
    @type map: List[List[TNode]]
       map[x][y] is a TNode with x-coordinate equal to x
       running from 0 to width-1
       and y-coordinate running from 0 to height-1
    @type treasure: TNode
       a navigable node in the map, the location of the treasure
    @type boat: TNode
       a navigable node in the map, the current location of the boat

    === Representation invariants ===
    - width and height are positive integers
    - map has dimensions width, height
    """

    def __init__(self, file_path, text_grid=None):
        """
        If text_grid is None, initialize a new Grid assuming file_path
        contains pathname to a text file with the following format:
        ..+..++
        ++.B..+
        .....++
        ++.....
        .T....+
        where a dot indicates a navigable TNode, a plus indicates a
        non-navigable TNode, B indicates the boat, and T the treasure.
        The width of this grid is 7 and height is 5.
        If text_grid is not None, it should be a list of strings
        representing a Grid. One string element of the list represents
        one row of the Grid. For example the grid above, should be
        stored in text_grid as follows:
        ["..+..++", "++.B..+", ".....++", "++.....", ".T....+"]

        @type file_path: str
           - a file pathname. See the above for the file format.
           - it should be ignored if text_grid is not None.
           - the file specified by file_path should exists, so there
             is no need for error handling
           Please call open_grid to open the file
        @type text_grid: List[str]
        @rtype: None
        """
        if text_grid != None:
            self.width = len(text_grid[0])
            self.height = len(text_grid)
            self.map = []

            for i in range(len(text_grid)):
                self.map.append([])
                for j in range(len(text_grid[i])):
                    if text_grid[i][j] == '.':
                        self.map[i].append(Node(True,j,i))
                    elif text_grid[i][j] == '+':
                        self.map[i].append(Node(False,j,i))
                    elif text_grid[i][j] == 'B':
                        self.map[i].append(Node(True,j,i))
                        self.boat = self.map[i][j]
                    elif text_grid[i][j] == 'T':
                        self.map[i].append(Node(True,j,i))
                        self.treasure = self.map[i][j]
        else:
            file = self.open_grid(file_path)
            i=0
            self.map = []
            for line in file:
                self.width = len(line)
                self.map.append([])
                for j in range(len(line)):
                    if line[j] == '.':
                        self.map[i].append(Node(True,j,i))
                    elif line[j] == '+':
                        self.map[i].append(Node(False,j,i))
                    elif line[j] == 'B':
                        self.map[i].append(Node(True,j,i))
                        self.boat = self.map[i][j]
                    elif line[j] == 'T':
                        self.map[i].append(Node(True,j,i))
                        self.treasure = self.map[i][j]
                i+=1
            self.height = i


    @classmethod
    def open_grid(cls, file_path):
        """
        @rtype TextIOWrapper:
        """
        return open(file_path)

    def __str__(self):
        """
        Return a string representation.

        @type self: Grid
        @rtype: str

        >>> g = Grid("", ["B.++", ".+..", "...T"])
        >>> print(g)
        B.++
        .+..
        ...T
        """
        # TODO
        st = ''

        for i in range(len(self.map)):
            for j in self.map[i]:
                if j.grid_x == self.boat.grid_x and j.grid_y == self.boat.grid_y:
                    st += 'B'
                elif j.grid_x == self.treasure.grid_x and j.grid_y == self.treasure.grid_y:
                    st += 'T'
                else:
                    st += j.__str__()
            st += '\n'
        return st

    def move(self, direction):
        """
        Move the boat in a specific direction, if the node
        corresponding to the direction is navigable
        Else do nothing

        @type self: Grid
        @type direction: str
        @rtype: None

        direction may be one of the following:
        N, S, E, W, NW, NE, SW, SE
        (north, south, ...)
        123
        4B5
        678
        1=NW, 2=N, 3=NE, 4=W, 5=E, 6=SW, 7=S, 8=SE
        >>> g = Grid("", ["B.++", ".+..", "...T"])
        >>> g.move("S")
        >>> print(g)
        ..++
        B+..
        ...T
        """
        # TODO
        boat_x = self.boat.grid_x
        boat_y = self.boat.grid_y

        try:
            if direction == 1 and self.map[boat_y-1][boat_x-1].navigable:
                if boat_x-1 < 0 or boat_y-1 < 0:
                    return None
                else:
                    self.boat = self.map[self.boat.grid_y-1][self.boat.grid_x-1]
            elif direction == 2 and self.map[boat_y-1][boat_x].navigable:
                if boat_y-1 < 0:
                    return None
                else:
                    self.boat = self.map[self.boat.grid_y-1][self.boat.grid_x]
            elif direction == 3 and self.map[boat_y-1][boat_x+1].navigable:
                if boat_y-1 < 0 or boat_x+1 > self.width:
                    return None
                else:
                    self.boat = self.map[self.boat.grid_y-1][self.boat.grid_x+1]
            elif direction == 4 and self.map[boat_y][boat_x-1].navigable:
                if boat_x-1 < 0:
                    return None
                else:
                    self.boat = self.map[self.boat.grid_y][self.boat.grid_x-1]
            elif direction == 5 and self.map[boat_y][boat_x+1].navigable:
                if boat_x+1 > self.width:
                    return None
                else:
                    self.boat = self.map[self.boat.grid_y][self.boat.grid_x+1]
            elif direction == 6 and self.map[boat_y+1][boat_x-1].navigable:
                if boat_x-1 < 0 or boat_y+1 > self.height:
                    return None
                else:
                    self.boat = self.map[self.boat.grid_y+1][self.boat.grid_x-1]
            elif direction == 7 and self.map[boat_y+1][boat_x].navigable:
                if boat_y+1 > self.height:
                    return None
                else:
                    self.boat = self.map[self.boat.grid_y+1][self.boat.grid_x]
            elif direction == 8 and self.map[boat_y+1][boat_x+1].navigable:
                if boat_x+1 > self.width or boat_y+1 > self.height:
                    return None
                else:
                    self.boat = self.map[self.boat.grid_y+1][self.boat.grid_x+1]
        except:
            return None



    def legal_node(self, x,y):
        if 0 <= x < self.width and 0 <= y < self.height and self.map[y][x].navigable:
            return True
        else:
            return False

    def give_walkable_squares(self, x,y, closed_list):
        walkable_squares = []

        if self.legal_node(x-1,y) and self.map[y][x-1] not in closed_list:
            walkable_squares.append(self.map[y][x-1])

        if self.legal_node(x,y-1) and self.map[y-1][x] not in closed_list:
            walkable_squares.append(self.map[y-1][x])

        if self.legal_node(x-1,y-1) and self.map[y-1][x-1] not in closed_list:
            walkable_squares.append(self.map[y-1][x-1])

        if self.legal_node(x+1,y) and self.map[y][x+1] not in closed_list:
            walkable_squares.append(self.map[y][x+1])

        if self.legal_node(x,y+1) and self.map[y+1][x] not in closed_list:
            walkable_squares.append(self.map[y+1][x])

        if self.legal_node(x+1,y+1) and self.map[y+1][x+1] not in closed_list:
            walkable_squares.append(self.map[y+1][x+1])

        if self.legal_node(x+1,y-1) and self.map[y-1][x+1] not in closed_list:
            walkable_squares.append(self.map[y-1][x+1])

        if self.legal_node(x-1,y+1) and self.map[y+1][x-1] not in closed_list:
            walkable_squares.append(self.map[y+1][x-1])
        return walkable_squares


    def find_path(self, start_node, target_node):
        """
        Implement the A-star path search algorithm
        If you will add a new node to the path, don't forget to set the parent.
        You can find an example in the docstring of TNode class
        Please note the shortest path between two nodes may not be unique.
        However all of them have same length!

        @type self: Grid
        @type start_node: TNode
           The starting node of the path
        @type target_node: TNode
           The target node of the path
        @rtype: None
        """
        # TODO
        #open list should be a priority queue with priority based on f-cost

        open_list = []
        closed_list = []
        #1) Add the starting square (or node) to the open list.
        open_list.append(start_node)
#        2) Repeat the following:
        while len(open_list) > 0:
            #a) Look for the lowest F cost square on the open list.
            #We refer to this as the current square.
            current = open_list[0]
            for node in open_list:
                if current.fcost() >= node.fcost():
                    current = node
#            b) Switch it to the closed list.
            del open_list[open_list.index(current)]
            closed_list.append(current)
            if target_node in closed_list:
                return None
            walk_squares = self.give_walkable_squares(current.grid_x, current.grid_y)
#            c) For each of the 8 squares adjacent to this current square …
#            If it is not walkable or if it is on the closed list, ignore it.
            working_list = []
            for el in walk_squares:
                if el not in closed_list:
                    working_list.append(el)
#            Otherwise do the following.
#            If it isn’t on the open list, add it to the open list.
            for mem in working_list:
#                    If it isn’t on the open list, add it to the open list. Make
#                   the current square the parent of this square.
#                   Record the F, G, and H costs of the square.
                if mem not in open_list:
                    open_list.append(mem)
                    mem.set_parent(current)
#                    print(current.grid_x, current.grid_y, 'current')
#                    print(mem.grid_x, mem.grid_y, 'mem')
                    mem.set_gcost(mem.distance(current) + current.distance(start_node))
                    mem.set_hcost(mem.distance(target_node))
                else:
#                If it is on the open list already, check to see if this path
#                to that square is better, using G cost as the measure.
                    this_path = mem.distance(current) + current.distance(start_node)
                    prev_path = mem.gcost
                    if this_path < prev_path:
                        print(current.grid_x, current.grid_y, 'current2')
                        print(mem.grid_x, mem.grid_y, 'mem2')
                        mem.set_parent(current)
                        mem.gcost = this_path

    def retrace_path(self, start_node, target_node):
        """
        Return a list of Nodes, starting from start_node,
        ending at target_node, tracing the parent
        Namely, start from target_node, and add its parent
        to the list. Keep going until you reach the start_node.
        If the chain breaks before reaching the start_node,
        return and empty list.

        @type self: Grid
        @type start_node: Node
        @type target_node: Node
        @rtype: list[Node]
        """
        # TODO
        path = []
        this_node = target_node
        while this_node != start_node:
            path.append(this_node)
            this_node.in_path = True
            this_node = this_node.parent
        path.append(start_node)
        start_node.in_path = True

    def get_treasure(self, s_range):
        """
        Return treasure node if it is located at a distance s_range or
        less from the boat, else return None
        @type s_range: int
        @rtype: TNode, None
        """
        # TODO
        if self.boat.distance(self.treasure) <= s_range:
            return self.treasure

    def plot_path(self, start_node, target_node):
        """
        Return a string representation of the grid map,
        plotting the shortest path from start_node to target_node
        computed by find_path using "*" characters to show the path
        @type self: Grid
        @type start_node: Node
        @type target_node: Node
        @rtype: str
        >>> g = Grid("", ["B.++", ".+..", "...T"])
        >>> print(g.plot_path(g.boat, g.treasure))
        B*++
        .+*.
        ...T
        """
        # TODO
        st = ''

        for i in range(len(self.map)):
            for j in self.map[i]:
                if j.grid_x == self.boat.grid_x and j.grid_y == self.boat.grid_y:
                    st += 'B'
                elif j.grid_x == self.treasure.grid_x and j.grid_y == self.treasure.grid_y:
                    st += 'T'
                elif j.in_path  == True:
                    st+='*'
                else:
                    st += j.__str__()
            st += '\n'
        return st
