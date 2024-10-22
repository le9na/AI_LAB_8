class AStar:
    def __init__(self):
        self.N = 12
        self.G = [[False] * self.N for _ in range(self.N)]
        self.setup_graph()
        self.est_cost = [float('inf')] * self.N  # heuristic costs
        self.setup_est_cost()
        self.to_city_cost = [[0] * self.N for _ in range(self.N)]  # costs between cities
        self.setup_city_costs()
        self.func_g_cost = [float('inf')] * self.N  # cost to reach each city
        self.func_f_cost = [float('inf')] * self.N  # estimated total cost
        self.parent = [-1] * self.N
        self.start = 0  # Buraydah
        self.goal = 5  # AlRass
        self.func_g_cost[self.start] = 0
        self.assign_f_cost(self.start)
        self.a_star()

    def setup_graph(self):
        edges = [(0, 1),
                 (0, 8),
                 (0, 4),
                 (1, 2),
                 (1, 3),
                 (2, 6),
                 (3, 4),
                 (3, 5),
                 (6, 7),
                 (8, 9),
                 (9, 10),
                 (10, 11)]
        for i, j in edges:
            self.G[i][j] = self.G[j][i] = True

    def setup_est_cost(self):
        # Heuristic costs (h(n))
        self.est_cost = [50, 70, 149, 164, 29, 0, 109, 239, 44, 52, 68, 74]

    def setup_city_costs(self):
        costs = {
            (0, 1): 86,
            (0, 8): 59,
            (0, 4): 150,
            (1, 2): 85,
            (1, 3): 45,
            (2, 6): 70,
            (3, 4): 95,
            (3, 5): 35,
            (6, 7): 60,
            (8, 9): 80,
            (9, 10): 75,
            (10, 11): 65
        }
        for (i, j), cost in costs.items():
            self.to_city_cost[i][j] = self.to_city_cost[j][i] = cost

    def h_func(self, i):
        return self.est_cost[i]

    def assign_f_cost(self, city):
        self.func_f_cost[city] = self.func_g_cost[city] + self.h_func(city)

    def a_star(self):
        open_set = set([self.start])
        closed_set = set()
        while open_set:
            current = min(open_set, key=lambda o: self.func_f_cost[o])
            print(f"Now expanding: {self.ret_city(current)}, g(n) = {self.func_g_cost[current]:.2f}, h(n) = {self.h_func(current):.2f}")
            if current == self.goal:
                self.print_path()
                return

            open_set.remove(current)
            closed_set.add(current)

            for neighbor in range(self.N):
                if self.G[current][neighbor] and neighbor not in closed_set:
                    temp_g = self.func_g_cost[current] + self.to_city_cost[current][neighbor]
                    if temp_g < self.func_g_cost[neighbor]:
                        self.parent[neighbor] = current
                        self.func_g_cost[neighbor] = temp_g
                        self.assign_f_cost(neighbor)
                        if neighbor not in open_set:
                            open_set.add(neighbor)
                            print(f"Reading {self.ret_city(neighbor)} for comparison, g(n) = {self.func_g_cost[neighbor]:.2f}, h(n) = {self.h_func(neighbor):.2f}, f(n) = {self.func_f_cost[neighbor]:.2f}\n")

    def print_path(self):
        path, current = [], self.goal
        while current != -1:
            path.append(self.ret_city(current))
            current = self.parent[current]
        path.reverse()
        print("\nGoal is Reached!\nFinal path: " + " > ".join(path))

    @staticmethod
    def ret_city(index):
        cities = ["Buraydah", "Unayzah", "AlZulfi",
                  "Al-Badai", "Riyadh-Alkhabra", "AlRass",
                  "UmSedrah", "Shakra", "Al-Bukayriyah",
                  "Sheehyah", "Dhalfa", "Mulida"]
        return cities[index]

if __name__ == "__main__":
    astar = AStar()
