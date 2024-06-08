import pytest
from a_search.maze.maze import Maze
import io


class TestMazePrint:
    @pytest.fixture
    def maze(self):
        return Maze("./test_files/maze2.txt")

    def test_print(self, monkeypatch, maze):
        test_output = io.StringIO()
        monkeypatch.setattr('sys.stdout', test_output)
        maze.print()

        expected_output = """
█A█
█ █
█B█

"""
        assert test_output.getvalue() == expected_output