import sys
import unittest
from data.tests.utils import mock_stdin, mock_stdouts, runner

module = open('data/tmp_files/Сильнее среднего.py', encoding='utf-8').read()


class TestCase1(unittest.TestCase):
    def test_1(self):
        inp = '5\n1\n2\n3\n4\n5\n'
        mock_stdin(self, inp)
        result = '<\n<\n0\n>\n>\n'

        mock_stdouts(self)
        runner(module)
        answer = sys.stdout.getvalue()
        if self.assertEqual(answer, result):
            self.counter += 1
        else:
            self.assertEqual(answer, result)

    def test_2(self):
        inp = '1\n1'
        mock_stdin(self, inp)
        result = '0\n'

        mock_stdouts(self)
        runner(module)
        answer = sys.stdout.getvalue()
        if self.assertEqual(answer, result):
            self.counter += 1
        else:
            self.assertEqual(answer, result)

    def test_3(self):
        inp = '5\n54\n3\n'
        mock_stdin(self, inp)
        result = '>\n<\n'

        mock_stdouts(self)
        runner(module)
        answer = sys.stdout.getvalue()
        if self.assertEqual(answer, result):
            self.counter += 1
        else:
            self.assertEqual(answer, result)


if __name__ == '__main__':
    unittest.main()
