import sys
import unittest
from data.tests.utils import mock_stdin, mock_stdouts, runner

module = open('data/tmp_files/Волшебный попугай.py', encoding='utf-8').read()


class TestCase1(unittest.TestCase):
    def test_1(self):
        inp = 'Привет друг\nКак дела\nЧто делаешь\n'
        mock_stdin(self, inp)
        result = 'Привет друг Кррр!\nКак дела Кррр!\nЧто делаешь Кррр!'

        mock_stdouts(self)
        runner(module)
        answer = sys.stdout.getvalue()
        if self.assertEqual(answer, result):
            self.counter += 1
        else:
            self.assertEqual(answer, result)

    def test_2(self):
        inp = '\n\n\n'
        mock_stdin(self, inp)
        result = ' Кррр!\n Кррр!\n Кррр!\n'

        mock_stdouts(self)
        runner(module)
        answer = sys.stdout.getvalue()
        if self.assertEqual(answer, result):
            self.counter += 1
        else:
            self.assertEqual(answer, result)

    def test_3(self):
        inp = 'fflfa\nfflfa\nfflfa\n'
        mock_stdin(self, inp)
        result = 'fflfa Кррр!\nfflfa Кррр!\nfflfa Кррр!'

        mock_stdouts(self)
        runner(module)
        answer = sys.stdout.getvalue()
        if self.assertEqual(answer, result):
            self.counter += 1
        else:
            self.assertEqual(answer, result)


if __name__ == '__main__':
    unittest.main()
