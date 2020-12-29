import pygame


class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = (255, 255, 255)
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.white = (255, 255, 255)
        self.orange = (255, 165, 0)
        self.black = (0, 0, 0)
        self.turquoise = (64, 224, 208)
        self.purple = (128, 0, 128)

    def get_position(self):
        return self.row, self.col

    def visited(self):
        return self.color == self.red

    def is_open(self):
        return self.color == self.green

    def is_barrier(self):
        return self.color == self.black

    def make_open(self):
        self.color = self.green

    def is_start(self):
        return self.color == self.orange

    def is_end(self):
        return self.color == self.turquoise

    def make_start(self):
        self.color = self.orange

    def make_visited(self):
        self.color = self.red

    def make_barrier(self):
        self.color = self.black

    def make_end(self):
        self.color = self.turquoise

    def make_path(self):
        self.color = self.purple

    def reset(self):
        self.color = self.white

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col - 1])

        if self.col > 0 and self.row > 0 and not grid[self.row-1][self.col-1].is_barrier():
            self.neighbors.append(grid[self.row-1][self.col-1])
        #
        # if self.col > 0 and self.row < self.total_rows - 1 and not grid[self.row-1][self.col+1].is_barrier():
        #     self.neighbors.append(grid[self.row-1][self.col+1])
        #
        # if self.col < self.total_rows-1 and self.row < self.total_rows - 1 and not grid[self.row+1][self.col+1].is_barrier():
        #     self.neighbors.append(grid[self.row+1][self.col+1])
        #
        # if self.col < self.total_rows-1 and self.row > 0 and not grid[self.row-1][self.col+1].is_barrier():
        #     self.neighbors.append(grid[self.row-1][self.col+1])
