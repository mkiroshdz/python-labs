from seed.random import Seeder as RandomSeeder
from seed.text import Seeder as TextSeeder

class Grid():
    @staticmethod
    def get_seeds(file):
        if file is None:
            seeder = RandomSeeder()
        else
            seeder = TextSeeder(file)

        return seeder.seeds();

    def is_valid_pos(self, (x, y)):
        return x >= 0 and y >= 0 and x <= self._max_x and y <= self._max_y

    def is_alive(self, (x, y)):
        idx = self.cells.index((x, y))
        return idx != -1 and self._states[idx]

    def neighbors(self, pos):
        valid_neighbor = lambda p: self.is_valid_pos(pos) and self.is_alive(pos)

        adjacent_cells = list(
            (x + 1, y), (x - 1, y),
            (x, y + 1), (x, y - 1)
        )

        return list(valid_neighbor, adjacent_cells)

    def status_in_next_generation(self, pos, alive):
        total_neighbors = self.neighbors(pos).count()
        
        alive_will_survive = alive and (total_neighbors == 2 or total_neighbors == 3)
        dead_will_reproduce = not(alive) and total_neighbors == 3

        alive_will_survive or dead_will_reproduce

    def __init__(self, file = None):
        cells = self.get_seeds(file)
        self.cells = cells
        self._states = [True for _ in cells]
        self._max_x = max(*[ x for (x, _) in cells]) 
        self._max_y = max(*[ y for (_, y) in cells])
    
    def tick():
        self.cells = [
            status_in_next_generation(c, self._states[idx])
            for (c, idx) in enumerate(self.cells)
        ]

    
