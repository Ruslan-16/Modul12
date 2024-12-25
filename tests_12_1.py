import test12
import unittest

class TestRunner(unittest.TestCase):
    def test_walk(self):
        runner = test12.Runner("Test Runner")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = test12.Runner("Test Runner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = test12.Runner("Runner 1")
        runner2 = test12.Runner("Runner 2")

        for _ in range(10):
            runner1.run()

        for _ in range(10):
            runner2.walk()

        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()