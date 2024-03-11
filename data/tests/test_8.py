import sys
import unittest
from data.tests.utils import mock_stdin, mock_stdouts, runner

module = open('data/tmp_files/Словари', encoding='utf-8').read()


class TestCase1(unittest.TestCase):
    def test_1(self):
        inp = '''3
        1 один\n
        2 два\n
        3 три\n
        3\n
        один\n
        три\n
        два\n
        \n'''
        mock_stdin(self, inp)
        result = '''1\n
        2\n
        3\n'''

        mock_stdouts(self)
        runner(module)
        answer = sys.stdout.getvalue()
        if self.assertEqual(answer, result):
            self.counter += 1
        else:
            self.assertEqual(answer, result)

    def test_2(self):
        inp = '''3
Пример Поступок, поведение или явление, служащее образцом для кого-л., чего-л.\n
Задача Цель, к которой стремятся, которую хотят достичь.\n
Учёба Процесс действия по значению глаг.: учиться.\n
4\n
Пример\n
Отличник\n
Задача\n
Пример\n'''
        mock_stdin(self, inp)
        result = '''Поступок, поведение или явление, служащее образцом для кого-л., чего-л.\n
Нет в словаре\n
Цель, к которой стремятся, которую хотят достичь.\n
Поступок, поведение или явление, служащее образцом для кого-л., чего-л.\n'''

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
