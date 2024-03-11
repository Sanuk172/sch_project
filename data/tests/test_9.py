import sys
import unittest
from data.tests.utils import mock_stdin, mock_stdouts, runner

module = open('data/tmp_files/Списки', encoding='utf-8').read()


class TestCase1(unittest.TestCase):
    def test_1(self):
        inp = '''сериал шерлок смотреть онлайн\n
                 учебник питона\n
                 мемы\n
                 социальная сеть\n
                 упражнения по питону\n
                 кормовые мыши для питонов\n
                 ответы егэ скачать бесплатно\n
                 компьютерные мыши\n
                 питон\n'''
        mock_stdin(self, inp)
        result = '''учебник питона\n
                    упражнения по питону\n
                    кормовые мыши для питонов\n'''

        mock_stdouts(self)
        runner(module)
        answer = sys.stdout.getvalue()
        if self.assertEqual(answer, result):
            self.counter += 1
        else:
            self.assertEqual(answer, result)

    def test_1(self):
        inp = '''zzzzzzzz\n
                 zxzx\n
                 zx\n
                 zxsvozx\n
                 1sv\n
                 1vo\n
                 2svo\n
                 3svo\n
                 svo\n'''
        mock_stdin(self, inp)
        result = '''zxsvozx\n
                    2svo\n
                    3svo\n'''

        mock_stdouts(self)
        runner(module)
        answer = sys.stdout.getvalue()
        if self.assertEqual(answer, result):
            self.counter += 1
        else:
            self.assertEqual(answer, result)


if __name__ == '__main__':
    unittest.main()
