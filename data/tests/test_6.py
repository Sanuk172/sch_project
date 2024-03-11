import sys
import unittest
from data.tests.utils import mock_stdin, mock_stdouts, runner

module = open('data/tmp_files/Четное нечетное', encoding='utf-8').read()


class TestCase1(unittest.TestCase):
    def test_1(self):
        inp = '203\n34\n52\nстоп'
        mock_stdin(self, inp)
        result = 'нечетное\nчетное\nчетное\n'

        mock_stdouts(self)
        runner(module)
        answer = sys.stdout.getvalue()
        if self.assertEqual(answer, result):
            self.counter += 1
        else:
            self.assertEqual(answer, result)

    def test_2(self):
        inp = '402934\nстоп\n'
        mock_stdin(self, inp)
        result = 'четное\n'

        mock_stdouts(self)
        runner(module)
        answer = sys.stdout.getvalue()
        if self.assertEqual(answer, result):
            self.counter += 1
        else:
            self.assertEqual(answer, result)


if __name__ == '__main__':
    unittest.main()
