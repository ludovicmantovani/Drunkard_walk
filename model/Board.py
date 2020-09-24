from random import randint

from model.Tile import *
from model import Direction


class Agent:
    def __init__(self):
        self.dead_probability = 0
        self.clone_probability = 0
        self.direction_probability = 25
        self.direction = Direction.get_random_direction()

    def move(self):
        if randint(0, 100) <= self.direction_probability:
            self.direction = Direction.get_random_direction()
        return self.direction


class Board:
    def __init__(self, size=10):
        self.size = size
        self.board = []
        self.agent = Agent()
        self.coverage = 50
        self.empty_tiles = None
        self.nbr_coverage_tiles = None
        self.set_size(self.size)
        #self.agent_position = int(self.size/2)-1, int(self.size/2)-1  # self.get_random_position()
        #self.board[self.agent_position[0]][self.agent_position[1]] = Tile.AGENT

    def set_agent(self, agent):
        self.agent = agent

    def set_size(self, size):
        self.size = size
        self.board.clear()
        self.empty_tiles = 1
        self.agent_position = int(self.size/2)-1, int(self.size/2)-1  # self.get_random_position()
        self.nbr_coverage_tiles = int(self.coverage/100 * self.size * self.size)
        # print(self.nbr_coverage_tiles)
        for line in range(0, size):
            new_line = []
            for column in range(0, size):
                if line == self.agent_position[0] and column == self.agent_position[1]:
                    new_line.append(Tile.EMPTY)
                else:
                    new_line.append(Tile.WALL)

            self.board.append(new_line)

    def get_random_position(self):
        line_index = randint(0, self.size)
        column_index = randint(0, self.size)
        return line_index, column_index

    def __len__(self):
        return len(self.board)

    def get_board(self):
        return self.board

    def generate(self, coverage):
        # if self.nbr_coverage_tiles == self.empty_tiles:
        self.coverage = coverage
        self.set_size(self.size)
        while self.nbr_coverage_tiles > self.empty_tiles:
            # print(str(self.empty_tiles) + '/' + str(self.nbr_coverage_tiles))
            futur_position = self.next_position(self.agent_position, self.agent.move())
            while futur_position[0] < 0 or futur_position[0] >= self.size or futur_position[1] < 0 or futur_position[1] >= self.size:
                futur_position = self.next_position(self.agent_position, self.agent.move())
            self.agent_position = futur_position
            if self.board[self.agent_position[0]][self.agent_position[1]] == Tile.WALL:
                self.empty_tiles = self.empty_tiles + 1
                self.board[self.agent_position[0]][self.agent_position[1]] = Tile.EMPTY

        #line_index, column_index = self.get_random_position()
        #tile = self.board[line_index][column_index]
        # if tile == Tile.WALL:
        #     self.board[line_index][column_index] = Tile.EMPTY
        # elif tile == Tile.EMPTY:
        #     self.board[line_index][column_index] = Tile.WALL

    def next_position(self, initial_position, direction):
        line_index, column_index = initial_position
        if direction == Direction.DirectionType.UP:
            return line_index-1, column_index
        elif direction == Direction.DirectionType.DOWN:
            return line_index+1, column_index
        elif direction == Direction.DirectionType.RIGHT:
            return line_index, column_index+1
        elif direction == Direction.DirectionType.LEFT:
            return line_index, column_index-1
        else:
            return line_index, column_index
