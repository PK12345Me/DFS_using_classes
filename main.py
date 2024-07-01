import itertools, sys, time, random

grid = [[1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]]


class Explored:

    def __init__(self) -> None:
        self._explored = []

    def add(self, val):
        self._explored.append(val)

    def nodes_explored(self):
        return self._explored


class FFrontier:
    def __init__(self, node=None) -> None:
        self._frontier = []
        # self._node = None

    def add(self, item):

        if isinstance(item, list):
            self._frontier.extend(item)
        else:
            self._frontier.append(item)

        print("this is the frontierList: ", self._frontier)

        time.sleep(1)
        while self._frontier:
            

            node = self._frontier[-1] #Preparing for LIFO

            if node in explored.nodes_explored():
                self._frontier = self._frontier[:-1] # LIFO implementation

            elif node == goal or explored.nodes_explored()[0] == goal:
                print("node is", node)
                print("Goal reached, code execution ended!")
                # break
                return

            elif node not in explored.nodes_explored():
                # print(f"to expand this {node} node")
                self._frontier = self._frontier[:-1] # LIFO implementation

                all_nodes.add_to_list(node)
                return


class Nodes_All:
    def __init__(self) -> None:
        self._check = []
        #self._direction = direction

    def add_to_list(self, value):

        direction = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
        self._check.clear()

        current = [
            (key1, key)
            for key1, value1 in enumerate(grid)
            for key, val in enumerate(value1)
            if val == value
        ]

        explored.add(grid[current[0][0]][current[0][1]])

        print("explored.nodes", explored.nodes_explored())

        for kya in direction:
            # print("direction is:", ky)
            ky = direction[kya]
            x = current[0][0] + ky[0]
            y = current[0][1] + ky[1]
            if 0 <= x < 3 and 0 <= y < 3:
                self._check.append(grid[x][y])

        return frontier.add(self._check)  # frontier(listCheck)

goal = random.randint(1, 9)
print("goal is: ", goal)
explored = Explored()
frontier = FFrontier()
all_nodes = Nodes_All()


def main():

    a = random.randint(1, 9)
    print("search starts with", a)
    all_nodes.add_to_list(a)

if __name =="__main__":
  main()
