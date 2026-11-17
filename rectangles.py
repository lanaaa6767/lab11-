# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 23:54:44 2026

@author: dell
"""

class Rectangle:
    def __init__(self, p, q):
        assert isinstance(p, Point) and isinstance(q, Point), "Bad input!"
        assert p.x <= q.x and p.y <= q.y, "Bad input!"
        self.p = p
        self.q = q

    def __str__(self):
        return f"(p={self.p}, q={self.q})"

    def get_width(self):
        return self.q.x - self.p.x

    def get_height(self):
        return self.q.y - self.p.y

    def perimeter(self):
        return 2 * (self.get_width() + self.get_height())

    def area(self):
        return self.get_width() * self.get_height()

    def contains(self, pt):
        assert isinstance(pt, Point), "Bad Input!"
        return (self.p.x <= pt.x <= self.q.x) and (self.p.y <= pt.y <= self.q.y)