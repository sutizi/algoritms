#!/usr/bin/env python3
import unittest

class Test_my_solution(unittest.TestCase):
    def not_repeated(self, s, pos):
        c = s[pos]
        pos = pos + 1
        unique = True
        while pos < len(s) and unique:
            unique = unique and s[pos] != c
            pos = pos +1
        return unique

    def solve(self, s):
        all_unique = True
        pos = 0
        while pos < len(s) and all_unique:
            all_unique = all_unique and self.not_repeated(s, pos)
            pos = pos +1
        return all_unique

    def __init__(self):
        self.assertTrue(self.solve('qwerty'))
        self.assertTrue(self.solve('asdfghjkl'))
        self.assertFalse(self.solve('qwertqwer'))
        self.assertFalse(self.solve('asdasdasd'))

t = Test_my_solution()
