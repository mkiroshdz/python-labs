import fileinput

class Seeder:
    def __init__(self, file):
        self._file = file

    def seeds(self):
        sds = list()
        with fileinput.input(files=(self._file,)) as f:
            for entry in f:
                x, sep, y = entry.partition(',')
                sds.append((int(x), int(y)))
        return sds