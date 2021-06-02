import tempfile
import os


class WrapStrToFile(object):
    def __init__(self):
        self.filepath = tempfile.mkstemp()
        self.file = None

    @property
    def content(self):
        fd, path = self.filepath
        f = open(path, 'r')
        try:
            self.file = f.read()
            return self.file
        except OSError(Exception):
            return "File doesn't exist yet"
        finally:
            f.close()

    @content.setter
    def content(self, value):
        fd, path = self.filepath
        f = open(path, 'w')
        self.file = f.write(value)
        f.close()

    @content.deleter
    def content(self):
        fd, path = self.filepath
        os.remove(path)


wstf = WrapStrToFile()

print(wstf.content)
wstf.content = 'test str'
print(wstf.content)
wstf.content = 'text 2'
print(wstf.content)
del wstf.content
