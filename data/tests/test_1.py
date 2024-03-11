import sys
import unittest
from utils import mock_stdin, mock_stdouts, runner

module = open('data/tmp_files/Волшебное число.py', encoding='utf-8').read()


class TestCase1(unittest.TestCase):
    def test_1(self):
        inp = '13\n'
        mock_stdin(self, inp)
        result = 'Брррр, холодрыга какая!\n'

        mock_stdouts(self)
        runner(module)
        answer = sys.stdout.getvalue()
        if self.assertEqual(answer, result):
            self.counter += 1
        else:
            self.assertEqual(answer, result)

    def test_2(self):
        inp = '42\n'
        mock_stdin(self, inp)
        result = 'Ура, сегодня мой день ведь я выиграл дом и 3 коровы.\n'

        mock_stdouts(self)
        runner(module)
        answer = sys.stdout.getvalue()
        if self.assertEqual(answer, result):
            self.counter += 1
        else:
            self.assertEqual(answer, result)

    def test_3(self):
        inp = '52\n'
        mock_stdin(self, inp)
        result = 'Ну булка хлеба, так булка хлеба.\n'

        mock_stdouts(self)
        runner(module)
        answer = sys.stdout.getvalue()
        if self.assertEqual(answer, result):
            self.counter += 1
        else:
            self.assertEqual(answer, result)


if __name__ == '__main__':
    unittest.main()
