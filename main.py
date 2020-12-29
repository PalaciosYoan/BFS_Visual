import pygame, sys
from node import Node


def reconstruct_path(came_from, node, draw):
    while node in came_from:
        node = came_from[node]
        if not node.is_start():
            node.make_path()
        draw()


def bfs(draw, start, end):
    queue = []
    path = {}
    queue.append(start)

    while queue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        currNode = queue.pop(0)

        if not currNode.is_start() and not currNode.is_end():
            currNode.make_visited()

        for neighbour in currNode.neighbors:
            if not neighbour.is_open() and not neighbour.visited() and not neighbour.is_start():
                if neighbour.is_end():
                    path[neighbour] = currNode
                    reconstruct_path(path, end, draw)
                    return True

                neighbour.make_open()
                path[neighbour] = currNode
                queue.append(neighbour)

        draw()


def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Node(i, j, gap, rows)
            grid[i].append(spot)

    return grid


def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, (255, 165, 165), (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, (255, 165, 165), (j * gap, 0), (j * gap, width))


def draw(win, grid, rows, width):
    win.fill((255, 255, 255))

    for row in grid:
        for node in row:
            node.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos
    row = y // gap
    col = x // gap
    return row, col


def main():
    width, height = 800, 800
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("DFS Path Finding Algorithm")

    rows = 50
    grid = make_grid(rows, width)

    start, end = None, None

    while True:
        draw(win, grid, rows, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pygame.mouse.get_pressed()[0]:  # LEFT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, rows, width)
                node = grid[row][col]
                if not start and node != end:
                    start = node
                    start.make_start()

                elif not end and node != start:
                    end = node
                    end.make_end()

                elif node != end and node != start:
                    node.make_barrier()

            elif pygame.mouse.get_pressed()[2]:  # RIGHT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, rows, width)
                node = grid[row][col]
                node.reset()
                if node == start:
                    start = None
                elif node == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)

                    bfs(lambda: draw(win, grid, rows, width), start, end)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(rows, width)


if __name__ == "__main__":
    main()
