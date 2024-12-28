import logging
import unittest
from runner import Runner

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s)s | %(message)s"
)

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        """Тестирование метода walk и обработка исключения ValueError"""
        try:
            runner = Runner(name="Vitek", speed=-20)  # Некорректная скорость
            runner.walk()
        except ValueError as e:
            logging.warning("Неверная скорость для Runner", exc_info=True)
            self.assertIsInstance(e, ValueError)  # Проверяем, что выбрасывается ValueError

    def test_run(self):
        """Тестирование метода run и обработка исключения TypeError"""
        try:
            runner = Runner(name=1, speed=20)  # Некорректное имя
            runner.run()
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)
            self.assertIsInstance(e, TypeError)  # Проверяем, что выбрасывается TypeError


if __name__ == "__main__":
    unittest.main()
