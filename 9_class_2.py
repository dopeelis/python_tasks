import time
import random


class Man(object):
    def __init__(self, name):
        self.name = name

    @staticmethod
    def solve_task():
        print("I' am not ready yet")


class Pupil(Man):
    def solve_task(self):
        sec = random.randint(3, 6)
        time.sleep(sec)
        print("I' am not ready yet")


Bob = Man('Bob')
Jack = Pupil('Jack')


Bob.solve_task()
Jack.solve_task()