import numpy as np
from numpy import mean
import random

params = {
    'world_size': (10, 10),
    'num_agents': 5,
    'same_pref': 0.5,
    'max_iter': 5
}

class Agent:
    def __init__(self, world, kind, preference):
        self.world = world
        self.kind = kind
        self.preference = preference
        self.location = None

    def move(self):
        if self.am_i_happy():
            return 0

        for patch in self.world.find_vacant(return_all=True):
            if self.am_i_happy(loc=patch):
                self.world.grid[self.location] = None
                self.location = patch
                self.world.grid[patch] = self
                return 1

        return 2

    def am_i_happy(self, loc=None, neighbor_check=False):
        loc = loc or self.location
        neighbors = self.locate_neighbors(loc)
        neighbor_kinds = [self.world.grid[patch].kind for patch in neighbors if self.world.grid[patch] is not None]

        if not neighbor_kinds:
            return False

        perc_like_me = sum(kind == self.kind for kind in neighbor_kinds) / len(neighbor_kinds)
        return perc_like_me >= self.preference

    def locate_neighbors(self, loc):
        x, y = loc
        neighbor_positions = [(x + dx, y + dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if (dx, dy) != (0, 0)]
        max_x, max_y = self.world.params['world_size'][0] - 1, self.world.params['world_size'][1] - 1

        def fix_edge(position):
            nx, ny = position
            return (nx % (max_x + 1), ny % (max_y + 1))

        return [fix_edge(pos) for pos in neighbor_positions]

class World:
    def __init__(self):
        self.params = params
        self.grid = self.build_grid(params['world_size'])
        self.agents = self.build_agents(params['num_agents'], params['same_pref'])
        self.reports = {'integration': []}
        self.init_world()

    def build_grid(self, world_size):
        return {(i, j): None for i in range(world_size[0]) for j in range(world_size[1])}

    def build_agents(self, num_agents, preference):
        kinds = ['red' if i < num_agents // 2 else 'blue' for i in range(num_agents)]
        random.shuffle(kinds)
        return [Agent(self, kind, preference) for kind in kinds]

    def init_world(self):
        for agent in self.agents:
            loc = self.find_vacant()
            self.grid[loc] = agent
            agent.location = loc
        assert sum(occupant is not None for occupant in self.grid.values()) == self.params['num_agents']

    def find_vacant(self, return_all=False):
        vacant_spots = [loc for loc, occupant in self.grid.items() if occupant is None]
        if return_all:
            return vacant_spots
        else:
            return random.choice(vacant_spots)

    def report_integration(self):
        diff_neighbors = [sum(not agent.am_i_happy(neighbor_check=True) for agent in self.agents)]
        self.reports['integration'].append(round(mean(diff_neighbors), 2))

    def run(self):
        for _ in range(self.params['max_iter']):
            random.shuffle(self.agents)
            move_results = [agent.move() for agent in self.agents]
            self.report_integration()

            num_happy_at_start = sum(result == 0 for result in move_results)
            num_moved = sum(result == 1 for result in move_results)
            num_stayed_unhappy = sum(result == 2 for result in move_results)

if __name__ == "__main__":
    world = World()
    world.run()
