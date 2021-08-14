#!/usr/bin/env python3
import unittest

class Test_my_solution(unittest.TestCase):

    def solve(self, s1, s2):
        """
        Retrun True if string s1 is a permutation of s2
        Keyword arguments:
            s1 -- string
            s2 -- string
        """
        if len(s1) != len(s2):
            return False
        index_1 = 0
        index_2 = len(s2) -1
        while index_1 < len(s1) and index_2 >= 0:
            if s1[index_1] != s2[index_2]:
                return False
            index_1+=1
            index_2-=1
        return True

    def __init__(self):
        self.assertTrue(self.solve('asdf', 'fdsa'))
        self.assertTrue(self.solve('qwertyuiop', 'poiuytrewq'))
        self.assertFalse(self.solve('qwertyuiop', 'poiurewq'))
        self.assertFalse(self.solve('asdf', 'fdea'))

t = Test_my_solution()
