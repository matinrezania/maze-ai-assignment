class Bidirectional_BFS_Search:
    def get_input(self):
        matrix = [list(map(int, input().split())) for i in range(8)]
        # print(matrix)
        '''
        input() takes a string as input. "1 2 3"
        split() splits the string by whitespaces and returns a
        list of strings. ["1", "2", "3"]
        list(map(int, ...)) transforms/maps the list of strings into a list of ints. [1, 2, 3]
        All these steps are done row times and these lists are stored in another list.[[1, 2, 3], [4, 5, 6], [7, 8, 9]], row = 3
        '''

        self.horizontal_matrix = matrix[0:4]
        self.vertical_matrix = matrix[4:8]
        # print(horizontal_matrix)
        # print(vertical_matrix)

    def __init__(self):
        self.forward_node = {"position": {"x": 1, "y": 1},
                             "path": [[1, 1]], "gn": 0, "parent_node": None}
        self.backward_node = {"position": {"x": 5, "y": 5},
                              "path": [[5, 5]], "gn": 0, "parent_node": None}
        self.goal_found = False
        self.forward_queue = []
        self.backward_queue = []

    def sort_queue(self, item):
        return item["gn"]

    def BFS(self, direction):
        if not self.goal_found:
            if direction == "forward":
                current_node = self.forward_node
                queue_nodes = self.forward_queue
            else:
                current_node = self.backward_node
                queue_nodes = self.backward_queue
            # move to right
            new_node = {"position": {"x": current_node["position"]["x"], "y": current_node["position"]["y"]+1},
                        "path": [*current_node["path"], [current_node["position"]["x"], current_node["position"]["y"]+1]],
                        "gn": current_node["gn"]+1,
                        "parent_node": current_node}

            # check wheter it can go right, check for obstacles and walls and duplicate
            if new_node["position"]["y"] != 6 and new_node not in queue_nodes and self.vertical_matrix[current_node["position"]["y"]-1][current_node["position"]["x"]-1] == 0:
                # this case is only for start node, which doesn't have a prent node
                if not current_node["parent_node"]:
                    queue_nodes.append(new_node)

                # for all nodes other than the start node
                elif new_node["position"] != current_node["parent_node"]["position"]:
                    queue_nodes.append(new_node)
            # move to left
            new_node = {"position": {"x": current_node["position"]["x"], "y": current_node["position"]["y"]-1},
                        "path": [*current_node["path"], [current_node["position"]["x"], current_node["position"]["y"]-1]],
                        "gn": current_node["gn"]+1,
                        "parent_node": current_node}

            # check wheter it can go left, check for obstacles and walls and duplicate
            # this case is only for start node, which doesn't have a prent node
            if new_node["position"]["y"] != 0 and new_node not in queue_nodes and self.vertical_matrix[current_node["position"]["y"]-2][current_node["position"]["x"]-1] == 0:
                if not current_node["parent_node"]:
                    queue_nodes.append(new_node)

                # for all nodes other than the start node
                elif new_node["position"] != current_node["parent_node"]["position"]:
                    queue_nodes.append(new_node)

            # move up
            new_node = {"position": {"x": current_node["position"]["x"]-1, "y": current_node["position"]["y"]},
                        "path": [*current_node["path"], [current_node["position"]["x"]-1, current_node["position"]["y"]]],
                        "gn": current_node["gn"]+1,
                        "parent_node": current_node}

            # check wheter it can go rigth, check for obstacles and walls and duplicate
            if new_node["position"]["x"] != 0 and new_node not in queue_nodes and self.horizontal_matrix[current_node["position"]["x"]-2][current_node["position"]["y"]-1] == 0:
                # this case is only for start node, which doesn't have a prent node
                if not current_node["parent_node"]:
                    queue_nodes.append(new_node)

                # for all nodes other than the start node
                elif new_node["position"] != current_node["parent_node"]["position"]:
                    queue_nodes.append(new_node)

            # move down
            new_node = {"position": {"x": current_node["position"]["x"]+1, "y": current_node["position"]["y"]},
                        "path": [*current_node["path"], [current_node["position"]["x"]+1, current_node["position"]["y"]]],
                        "gn": current_node["gn"]+1,
                        "parent_node": current_node}

            # check wheter it can go rigth, check for obstacles and walls and duplicate
            # this case is only for start node, which doesn't have a prent node
            if new_node["position"]["x"] != 6 and new_node not in queue_nodes and self.horizontal_matrix[current_node["position"]["x"]-1][current_node["position"]["y"]-1] == 0:
                if not current_node["parent_node"]:
                    queue_nodes.append(new_node)

                # for all nodes other than the start node
                elif new_node["position"] != current_node["parent_node"]["position"]:
                    queue_nodes.append(new_node)

            if queue_nodes == []:
                self.goal_found = True
                print("answer not found")

            # to get the best choice, the choice with lowest cost
            # print("queu is :", queue_nodes)
            queue_nodes.sort(key=self.sort_queue)
            choice = queue_nodes[0]
            del queue_nodes[0]
            # updating the position
            current_node = choice
            if direction == "forward":
                self.forward_node = current_node
                self.forward_queue = queue_nodes
            else:
                self.backward_node = current_node
                self.backward_queue = queue_nodes

            self.intersect()

    def intersect(self):
        if [self.backward_node["position"]["x"], self.backward_node["position"]["y"]] in self.forward_node["path"]:
            self.goal_found = True

    def search(self):
        while not self.goal_found:
            self.BFS(direction="forward")
            self.BFS(direction="backward")
        self.build_goal_path()

    def build_goal_path(self):
        self.backward_node["path"].reverse()
        path = [*self.forward_node["path"],
                *self.backward_node["path"]]
        self.goal_path = []
        [self.goal_path.append(node)
         for node in path if node not in self.goal_path]


graph = Bidirectional_BFS_Search()
graph.get_input()
graph.search()

print("best path:", end=" ")
for node in graph.goal_path:
    print(node, end=" ")
