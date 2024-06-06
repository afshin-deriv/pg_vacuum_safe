import unittest
from src.vacuum_tool import run_vacuum


class TestVacuumTool(unittest.TestCase):
    def test_run_vacuum(self):
        # Example test case
        try:
            run_vacuum()
        except Exception as e:
            self.fail(f"run_vacuum() raised {e} unexpectedly!")


if __name__ == '__main__':
    unittest.main()
