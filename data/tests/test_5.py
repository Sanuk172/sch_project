import sys
import unittest
from data.tests.utils import mock_stdin, mock_stdouts, runner

module = open('data/tmp_files/Поиск маны.py', encoding='utf-8').read()


class TestCase1(unittest.TestCase):
    def test_1(self):
        inp = 'bujdshfbgМана\nстоп\n'
        mock_stdin(self, inp)
        result = 'абра кадабра\n'

        mock_stdouts(self)
        runner(module)
        answer = sys.stdout.getvalue()
        if self.assertEqual(answer, result):
            self.counter += 1
        else:
            self.assertEqual(answer, result)

    def test_2(self):
        inp = 'bujdshfbgмана\nстоп\n'
        mock_stdin(self, inp)
        result = 'абра кадабра\n'

        mock_stdouts(self)
        runner(module)
        answer = sys.stdout.getvalue()
        if self.assertEqual(answer, result):
            self.counter += 1
        else:
            self.assertEqual(answer, result)

    def test_3(self):
        inp = '52\nстоп\n'
        mock_stdin(self, inp)
        result = 'НЕТ\n'

        mock_stdouts(self)
        runner(module)
        answer = sys.stdout.getvalue()
        if self.assertEqual(answer, result):
            self.counter += 1
        else:
            self.assertEqual(answer, result)


if __name__ == '__main__':
    unittest.main()
