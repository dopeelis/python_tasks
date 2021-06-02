import time


class Count(object):
    def __enter__(self):
        self.start = time.perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop = time.perf_counter()
        time_func = self.stop - self.start
        print(f'Function running time: {time_func} seconds')


with Count():
    a = 1 + 25
    print(a)

