import heapq

# Define the puzzle state class
class PuzzleState:
    def __init__(self, state, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = 0
        
        if self.parent:
            self.cost = self.parent.cost + 1

    # Compare states
    def __eq__(self, other):
        return self.state == other.state

    # Define the less than operator
    def __lt__(self, other):
        return self.cost < other.cost

    # Hash the state
    def __hash__(self):
        return hash(str(self.state))

    # Get the position of the blank space
    def get_blank_position(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return (i, j)

# Get possible moves from a state
def get_children(state):
    children = []
    blank_position = state.get_blank_position()
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for move in moves:
        new_x = blank_position[0] + move[0]
        new_y = blank_position[1] + move[1]

        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in state.state]
            new_state[blank_position[0]][blank_position[1]] = new_state[new_x][new_y]
            new_state[new_x][new_y] = 0
            children.append(PuzzleState(new_state, state, move))

    return children

# Define the heuristic function
def heuristic(state, target):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != target[i][j]:
                count += 1
    return count

# Implement the A* algorithm
def a_star(start_node, target_state):
    open_list = []
    closed_list = set()

    heapq.heappush(open_list, start_node)

    while open_list:
        current_state = heapq.heappop(open_list)

        if current_state.state == target_state:
            path = []
            while current_state:
                path.append((current_state.state, current_state.move))
                current_state = current_state.parent
            return path[::-1]

        closed_list.add(current_state)

        for child in get_children(current_state):
            if child in closed_list:
                continue

            child.cost += heuristic(child.state, target_state)

            if child not in open_list:
                heapq.heappush(open_list, child)
            elif child in open_list and child.cost < open_list[open_list.index(child)].cost:
                open_list.remove(child)
                heapq.heappush(open_list, child)

    return None

# Example usage:
start_state = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
target_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

start_node = PuzzleState(start_state)
target_node = PuzzleState(target_state)

path = a_star(start_node, target_state)

if path:
    for i, (state, move) in enumerate(path):
        print(f"Step {i + 1}: Move {move} =>")
        for row in state:
            print(row)
        print()
else:
    print("No solution found.")
