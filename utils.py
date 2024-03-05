import io
import sys


def mock_stdin(testcase_inst, inputs):
    stdin = sys.stdin

    def cleanup():
        sys.stdin = stdin

    testcase_inst.addCleanup(cleanup)
    sys.stdin = io.StringIO(inputs)


def mock_stdouts(testcase_inst):
    stderr = sys.stderr
    stdout = sys.stdout

    def cleanup():
        sys.stderr = stderr
        sys.stdout = stdout

    testcase_inst.addCleanup(cleanup)
    sys.stderr = io.StringIO()
    sys.stdout = io.StringIO()


def input_output(module, testcase, inp: str):
    mock_stdin(testcase, inp)
    mock_stdouts(testcase)
    runner(module)
    return sys.stdout.getvalue()


def runner(module):
    exec(module)
