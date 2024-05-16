import pytest
from a_search.maze.maze import Maze


class TestMaze:

    @pytest.fixture(scope='class')
    def maze(self):
        return Maze("./test_files/maze1.txt")

    def test_init(self, maze):
        assert maze.height == 10, "Height should be 10 for simple_maze.txt"
        assert maze.width == 10, "Width should be 10 for simple_maze.txt"
        assert maze.start == (9, 0), "Start should be at (1, 1) for simple_maze.txt"
        assert maze.goal == (0, 5), "Goal should be at (8, 8) for simple_maze.txt"

    def test_solve(self, maze):
        maze.solve()
        solution_actions, solution_cells = maze.solution
        assert solution_actions[0] == "up", "Solution should start with 'down' action"
        assert solution_cells[0] == (8, 0), "Solution should start with cell (2, 1)"
        assert solution_actions[-1] == "up", "Solution should end with 'right' action"
        assert solution_cells[-1] == (0, 5), "Solution should end with goal cell (8, 8)"

    def test_neighbors(self, maze):
        neighbors = maze.neighbors((9, 0))
        expected_neighbors = [('up', (8, 0))]
        assert neighbors == expected_neighbors, "Neighbors of cell (1,1) should be " + str(expected_neighbors)
