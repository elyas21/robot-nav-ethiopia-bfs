
state_space_graph_et = {
    'Awash': ['Chiro','Matahara'],
    'Assasa':['Assella','Dodolla'],
    'Debre_Birhan':['Addis_Abeba'],
    'Dembi_Dollo': ['Gimbi','Gambella'],
    'Chiro':['Awash', 'Dire_Dawa'],
    'Matahara':['Awash','Adama'],
    'Dire_Dawa': ['Chiro','Harar'],
    'Adama': ['Matahara','Addis_Abeba','Batu','Assella'],
    'Addis_Abeba':['Debre_Birhan','Adama','Ambo'],
    'Harar':['Dire_Dawa','Babile'],
    'Batu': ['Buta_Jirra','Adama','Shashemene'],
    'Assella':['Adama','Assasa'],
    'Ambo':['Addis_Abeba','Nekemete','Wolkite'],
    'Babile':['Harar','Jigjiga'],
    'Buta_Jirra':['Batu','Worabe'],
    'Shashemene': ['Batu','Hossana','Dodolla','Hawassa'],
    'Gimbi':['Dembi_Dollo','Nekemete'],
    'Gambella': ['Dembi_Dollo','Gore'],
    'Nekemete': ['Gimbi','Ambo','Bedelle'],
    'Wolkite':['Ambo','Worabe','Jimma'],
    'Jigjiga':['Babile','Dega_Habur'],
    'Worabe': ['Buta_Jirra','Wolkite','Hossana'],
    'Hossana':['Shashemene','Worabe', 'Wolaita_Sodo'],
    'Dodolla':['Assasa','Bale','Shashemene'],
    'Hawassa':['Shashemene','Dilla'],
    'Gore':['Gambella','Tepi','Bedelle'],
    'Bedelle': ['Nekemete','Jimma','Gore'],
    'Jimma':['Wolkite','Bedelle','Bonga'],
    'Dega_Habur':['Jigjiga','Goba','Kebri_Dehar'],
    'Wolaita_Sodo': ['Hossana','Dawro','Arba_Minch'],
    'Bale':['Dodolla','Goba','Sof_Oumer'],
    'Dilla': ['Hawassa'],
    'Kebri_Dehar':['Sof_Oumer','Gode'],
    'Gode':['Kebri_Dehar'],
    'Arba_Minch':['Wolaita_Sodo'],
    'Sof_Oumer':['Kebri_Dehar','Goba','Bale'],
    'Bonga':['Jimma','Tepi','Mezan_Teferi','Dawro'],
    'Dawro':['Bonga','Wolaita_Sodo'],
    'Tepi': ['Mezan_Teferi' , 'Gore', 'Bonga'],
    'Mezan_Teferi':['Tepi', 'Bonga'],
    'Goba': ['Sof_Oumer', 'Bale', 'Dega_Habur']
}

city_map = {
    'Addis_Abeba':(0.01,0.0),
    'Debre_Birhan':(4.4,-2.3),
    'Matahara':(-1.4,-3.02),
    'Awash': (-1.5,-6.05),
    'Chiro':(-1.4,-10.19),
    'Dire_Dawa': (-1.81, -14.55),
    'Adama': (-2.99,-1.3),
    'Harar':(1.1,-17.67),
    'Babile':(-0.97,-22.0),
    'Jigjiga':(-2.6, -24.62),
    'Dega_Habur':(-5.99,-27.40),
    'Kebri_Dehar':(-12.32,-28.09),
    'Gode':(-17.35, -26.24),
    'Sof_Oumer':(-17.71, -16.15),
    'Goba': (-17.46, -13.63),
    'Bale':(-21.13,-10.74),
    'Dodolla':(-23.4,-5.78),
    'Assasa':(-21.08,-2.81),
    'Assella':(-18.25,-0.61),
    'Batu': (-24.05,4.97),
    'Buta_Jirra':(-21.85,7.53),
    'Worabe': (-25.67,10.60),
    'Hossana':(-29.2,13.32),
    'Wolaita_Sodo': (-31.05, 11.36),
    'Arba_Minch':(-34.71, 13.03),
    'Dilla': (-33.40, 6.84),
    'Hawassa':(-30.8,7.23),
    'Shashemene': (-27.82,7.81),
    'Dawro':(-33.32, 18.97),
    'Bonga':(-31.19,21.2),
    'Mezan_Teferi':(-34.37, 23.26),
    'Tepi':(-34.25, 26.54),
    'Gore':(-32.72,28,74),
    'Gambella': (-33.87,32.41),
    'Dembi_Dollo': (-28.39,28.99),
    'Gimbi':(-26.8, 23.72),
    'Nekemete':(-26.63,18.51),
    'Bedelle': (-30.02,19.50),
    'Jimma':[-31.85,17.46],
    'Wolkite':(-29.21, 14.20),
    'Ambo': (-26.58, 10,95),



}
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty")

    def size(self):
        return len(self.items)

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty")

    def size(self):
        return len(self.items)



class Searcher:

    def __init__(self, state_space_graph, initial_state, goal_state):
        self.graph = state_space_graph
        self.initial_state = initial_state
        self.goal_state = goal_state

    def search(self, strategy):
        """
        Performs a search using the specified strategy.
        :param strategy: "bfs" or "dfs"
        :return: The path from the initial state to the goal state,
                or None if the goal state is not found.
        """
        if strategy == "bfs":
            return self.breadth_first_search()
        elif strategy == "dfs":
            return self.depth_first_search()
        else:
            raise ValueError("Invalid search strategy:", strategy)
    def breadth_first_search(self):
        """
        Performs a Breadth-First Search (BFS) on the state space graph.
        :return: The path from the initial state to the goal state,
                or None if the goal state is not found.
        """
        visited = set()
        queue = Queue()
        queue.enqueue((self.initial_state, []))

        while not queue.is_empty():
            state, path = queue.dequeue()
            visited.add(state)

            if state == self.goal_state:
                return path + [state]

            for neighbor in self.graph[state]:
                if neighbor not in visited:
                    queue.enqueue((neighbor, path + [state]))

        return None

    def depth_first_search(self):
        """
        Performs a Depth-First Search (DFS) on the state space graph.
        :return: The path from the initial state to the goal state,
                or None if the goal state is not found.
        """
        visited = set()
        stack = Stack()
        stack.push((self.initial_state, []))

        while not stack.is_empty():
            state, path = stack.pop()
            visited.add(state)

            if state == self.goal_state:
                return path + [state]

            for neighbor in self.graph[state]:
                if neighbor not in visited:
                    stack.push((neighbor, path + [state]))

        return None

def map_coordinates(path):
    """
    Maps city names in the path to their coordinates using the city_map dictionary.
    :param path: The path from the initial state to the goal state.
    :return: A list of dictionaries with 'x' and 'y' keys corresponding to the cities in the path.
    """
    return [{'x': city_map[city][0], 'y': city_map[city][1]} for city in path]

def path_finder(initial_state, goal_state):
    searcher = Searcher(state_space_graph_et, initial_state, goal_state)
    bfs_path = searcher.search("bfs")

    if bfs_path is not None:
        coordinates_path = map_coordinates(bfs_path)
        return coordinates_path
    else:
        return None


# print(path_finder('Addis_Abeba' , 'Harar'))
