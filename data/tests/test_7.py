import sys
import unittest
from data.tests.utils import mock_stdin, mock_stdouts, runner

module = open('data/tmp_files/Множества', encoding='utf-8').read()


class TestCase1(unittest.TestCase):
    def test_1(self):
        inp = '3\nМосква\nНью-Йорк\nЛондон\nПариж\n'
        mock_stdin(self, inp)
        result = 'OK\n'

        mock_stdouts(self)
        runner(module)
        answer = sys.stdout.getvalue()
        if self.assertEqual(answer, result):
            self.counter += 1
        else:
            self.assertEqual(answer, result)

    def test_2(self):
        inp = '3\nМосква\nНью-Йорк\nЛондон\nМосква\n'
        mock_stdin(self, inp)
        result = 'TRY ANOTHER\n'

        mock_stdouts(self)
        runner(module)
        answer = sys.stdout.getvalue()
        if self.assertEqual(answer, result):
            self.counter += 1
        else:
            self.assertEqual(answer, result)


if __name__ == '__main__':
    unittest.main()
