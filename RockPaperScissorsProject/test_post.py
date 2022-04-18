import urllib.parse
import urllib.request
import html
import re
import os
import io
import sys
import importlib
import traceback
from contextlib import redirect_stdout
import importlib.util
import threading

_DEBUG = False

char_limit = 5000  # limit the characters in output

_input = input
errors = 0

def input(p = None):
    try:
        x = _input(p)
    except EOFError:
        raise EOFError("You program is trying to input user input, but there is no more userinput in the test")
    print(x)
    return x

class Post:
    def __init__(self, file_name, program):
        if not os.path.isfile(file_name):
            raise FileExistsError()
        self.file_name = file_name
        self.program = program
        self.name = ''
        self.email = ''
        self.passed = False
        self.output = ''
        self.post_url = 'http://cbis2.lbcc.edu/cs22/cs22postdb.php/' # 'http://sbox/cs22postdb.php/'
        if _DEBUG: self.post_url = 'http://sbox/cs22postdb.php/'

    def __repr__(self):
        return \
            "name: " + self.name + "\n" \
            "email: " + self.email + "\n" \
            "program: " + self.program + "\n" \
            "file_name: " + self.file_name + "\n"

    def _parse_headers(self):
        buf = ''
        with open(self.file_name, 'r') as fin:
            for i in range(1, 6):
                l = fin.readline().strip()
                if l == '':
                    buf += ' <eof>'
                    break  # end of file
                if l[0] == '#':
                    buf += l[1:] + ' <nl> '
        words = re.split(r"\s+", buf)
        # throw out only symbols
        words = list(filter(lambda x: re.search(r'[A-Za-z]', x), words))
        for i, word in enumerate(words):
            if re.match(r'\w*name\w*', word, re.IGNORECASE):
                j = i + 1
                self.name = words[j]
                j += 1
                while words[j] != '<nl>' and \
                        not re.match(r'\w*email\w*', words[j], re.IGNORECASE) and \
                            words[j] != "<eof>":
                    self.name += " " + words[j]
                    j += 1
                break

        for i, word in enumerate(words):
            if re.match(r'\w*email\w*', word, re.IGNORECASE):
                self.email = words[i + 1]
                break

    def do_post(self):
        ''' Parse name, email from file '''

        self._parse_headers()

        values = {'name': self.name,
                  'email': self.email,
                  'program': self.program,
                  'file_name': self.file_name,
                  'file': open(self.file_name, 'r').read(),
                  # limit # chars in case of loops
                  'output': self.output[:char_limit],
                  'passed': self.passed
                  }  # fields to post

        data = urllib.parse.urlencode(values)
        data = data.encode('ascii')
        # Send HTTP POST request
        req = urllib.request.Request(self.post_url, data)
        with urllib.request.urlopen(req) as response:
            the_page = html.unescape(response.read().decode("utf-8"))
            the_page = the_page.replace("\\n", "\n")

        # Print the result
        print(the_page)


def assert_output_contains(out, pattern, msg=None):
    if msg is None:
        msg = "Your output does not contain '{}' pattern".format(pattern)
    m = re.search(pattern, out)
    if m is None:
        print("ERROR: " + msg)
        return False
    return True

def t_run(module_name, path):
    exec(open(path).read(), globals())
    # spec = importlib.util.spec_from_file_location(module_name, path)
    # mod = importlib.util.module_from_spec(spec)
    # # read python file and get output in buf
    # spec.loader.load_module(mod)

def _run(file_name, dir='.', stdin=None, time=5.0):  # run non-interactive py file  and return output
    global errors
    if dir == '.':
        dir = os.getcwd()  # current directory full path with /
    else:
        if dir[-1] != '\\' and dir[-1] != r'/':
            dir = dir + '/'
    module_name = file_name.split('.')[0]

    with io.StringIO() as buf, redirect_stdout(buf):
        if stdin:
            in_buf = io.StringIO(stdin)
            sys.stdin = in_buf

        py_file = "{}/{}".format(dir, file_name)
        try:  # import user file to run
            t = threading.Thread(target=t_run,args = (module_name, py_file),daemon = True)
            t.start()
            t.join(timeout=float(time))
            if t.is_alive():
                raise TimeoutError("Your program timed out due to waiting for input, or a infinite loop")
            #t_run(module_name,py_file)
            # spec = importlib.util.spec_from_file_location(module_name, py_file)
            # foo = importlib.util.module_from_spec(spec)
            # # read python file and get output in buf
            # spec.loader.exec_module(foo)
        except:
            msg = '*** A compile or runtime error occured in your python' \
                  ' file, see last few lines of traceback for why:'
            msg += '\n' + traceback.format_exc()
            errors += 1
            return False, msg + '\n' + buf.getvalue()
        if stdin:
            sys.stdin = sys.__stdin__ #restore stdin

        return True, buf.getvalue()


def run(file_name, dir='.', test=None, stdin=None, time=5.0, output=True):
    global errors
    errors = 0
    ran, out = _run(file_name, dir,stdin=stdin, time=time)

    if output or not ran:
        print('-- YOUR OUTPUT', '-' * 20)
        print(out)
        print("-"*35 + "\n")

    if not ran: errors += 1

    p = Post(file_name, file_name.split('.')[0])
    p.output = out
    if ran and test:
        errors = test(out)
        print("*** Your program had {} errors".format(errors))
        print("\n" + "-"*35 + "\n")
        if errors == 0:
            p.passed = True
    else:
        p.passed = False
    p.do_post()

if __name__ == "__main__":
    report = Post(
        "/Users/gjenkins/Dropbox/PycharmProjects/cs22_asssignments/hello.py",
        "Hello")
    report.do_post()
