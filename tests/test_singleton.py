import random

from singleton import __version__, Singleton


def test_version():
    assert __version__ == '0.1.0'


class A(metaclass=Singleton):
    def __init__(self):
        self.banana = random.randint(1, 100)


def test_same_instance():
    a = A()
    b = A()
    assert a.banana == b.banana
    assert a is b
