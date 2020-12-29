import pygame
from node import Node


class Grid:
    def __init__(self, rows, width):
        self.grid = []
        self.gap = width // rows
        self.rows = rows
        self.width = width
        for i in range(rows):
            self.grid.append([])
            for j in range(rows):
                node = Node(i, j, self.gap, rows)
                self.grid[i].append(node)

    def get_node(self, row, col):
        return self.grid[row][col]

    def update_neighbors(self):
        for row in self.grid:
            for node in row:
                node.update_neighbors(self.grid)

    def reset(self, rows, width):
        self.grid = []
        self.gap = width // rows
        self.rows = rows
        self.width = width
        for i in range(rows):
            self.grid.append([])
            for j in range(rows):
                node = Node(i, j, self.gap, rows)
                self.grid[i].append(node)

    def draw(self, win):
        for row in self.grid:
            for node in row:
                node.draw(win)

        for i in range(self.rows):
            pygame.draw.line(win, (255, 165, 165), (0, i * self.gap), (self.width, i * self.gap))
            for j in range(self.rows):
                pygame.draw.line(win, (255, 165, 165), (j * self.gap, 0), (j * self.gap, self.width))
