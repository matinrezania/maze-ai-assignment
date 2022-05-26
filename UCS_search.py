matrix = [list(map(int, input().split())) for i in range(8)]
print(matrix)
'''
input() takes a string as input. "1 2 3"
split() splits the string by whitespaces and returns a
list of strings. ["1", "2", "3"]
list(map(int, ...)) transforms/maps the list of strings into a list of ints. [1, 2, 3]
All these steps are done row times and these lists are stored in another list.[[1, 2, 3], [4, 5, 6], [7, 8, 9]], row = 3
'''

horizontal_matrix = matrix[0:4]
vertical_matrix = matrix[4:8]
print(horizontal_matrix)
print(vertical_matrix)


current_node = {"position": {"x": 1, "y": 1},
                "path": [[1, 1]], "gn": 0, "parent_node": None}
queue_nodes = []


def sort_queue(item):
    # print(item)
    return item["gn"]


while True:
    # move to right
    new_node = {"position": {"x": current_node["position"]["x"], "y": current_node["position"]["y"]+1},
                "path": [*current_node["path"], [current_node["position"]["x"], current_node["position"]["y"]+1]],
                "gn": current_node["gn"]+1,
                "parent_node": current_node}
    print(new_node["position"], new_node["parent_node"]["position"])

    # check wheter it can go right, check for obstacles and walls and duplicate
    if new_node["position"]["y"] != 6 and new_node not in queue_nodes and vertical_matrix[current_node["position"]["y"]-1][current_node["position"]["x"]-1] == 0:
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
    if new_node["position"]["y"] != 0 and new_node not in queue_nodes and vertical_matrix[current_node["position"]["y"]-2][current_node["position"]["x"]-1] == 0:
        if not current_node["parent_node"]:
            queue_nodes.append(new_node)

        # for all nodes other than the start node
        elif new_node["position"] != current_node["parent_node"]["position"]:
            queue_nodes.append(new_node)

    # move up
    new_node = {"position": {"x": current_node["position"]["x"]-1, "y": current_node["position"]["y"]},
                "path": [*current_node["path"], [current_node["position"]["x"]-1, current_node["position"]["y"]]],
                "gn": current_node["gn"]+3,
                "parent_node": current_node}

    # check wheter it can go rigth, check for obstacles and walls and duplicate
    if new_node["position"]["x"] != 0 and new_node not in queue_nodes and horizontal_matrix[current_node["position"]["x"]-2][current_node["position"]["y"]-1] == 0:
        # this case is only for start node, which doesn't have a prent node
        if not current_node["parent_node"]:
            queue_nodes.append(new_node)

        # for all nodes other than the start node
        elif new_node["position"] != current_node["parent_node"]["position"]:
            queue_nodes.append(new_node)

    # move down
    new_node = {"position": {"x": current_node["position"]["x"]+1, "y": current_node["position"]["y"]},
                "path": [*current_node["path"], [current_node["position"]["x"]+1, current_node["position"]["y"]]],
                "gn": current_node["gn"]+3,
                "parent_node": current_node}

    # check wheter it can go rigth, check for obstacles and walls and duplicate
    # this case is only for start node, which doesn't have a prent node
    if new_node["position"]["x"] != 6 and new_node not in queue_nodes and horizontal_matrix[current_node["position"]["x"]-1][current_node["position"]["y"]-1] == 0:
        if not current_node["parent_node"]:
            queue_nodes.append(new_node)

        # for all nodes other than the start node
        elif new_node["position"] != current_node["parent_node"]["position"]:
            queue_nodes.append(new_node)

    if queue_nodes == []:
        break

    queue_nodes.sort(key=sort_queue)

    # to get the best choice, the choice with lowest cost
    # print("queu is :", queue_nodes)
    choice = queue_nodes[0]
    del queue_nodes[0]
    # updating the position
    current_node = choice

    # goal test case
    if current_node["position"] == {"x": 5, "y": 5}:
        print("goal has been reached")
        break

    # print("choice is: ", choice)

print("best path: ", current_node["path"], "path cost: ", current_node["gn"])
