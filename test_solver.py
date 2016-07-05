from unittest import TestCase
from Solver import Solver

__author__ = 'ONicholls'


class TestSolver(TestCase):

    def test_negative_discr(self):  # throwing an exception, if the discriminant of a quadratic equation is negative

        s = Solver
        self.assertRaises(Exception, s.demo, 2, 1, 2)

    # def test_demo(self):
    #
    #     self.fail()