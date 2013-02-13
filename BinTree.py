#!/usr/bin/env python

import random

debug = False

r_min = 0
r_max = 99
eles = 100
ele_list = []

class BinTree(object):
    bias = 'left'
    def __init__(self, value, parent=None, *args):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None
        if args:
            for arg in args:
                self.add(arg)
    def add(self, value):
        if debug:
            print 'Adding value \'%s\'' % value
        if value <= self.value:
            if self.left:
                self.left.add(value)
            else:
                self.left = BinTree(value, parent=self)
        else:
            if self.right:
                self.right.add(value)
            else:
                self.right = BinTree(value, parent=self)
    def __str__(self):
        value = str(self.value)
        value_char_len = len(value)
        left = ('', str(self.left))[bool(self.left)]
        right = ('', str(self.right))[bool(self.right)]
        left_list = ([], left.split('\n'))[bool(self.left)]
        right_list = ([], right.split('\n'))[bool(self.right)]
        lines = max((len(left_list), len(right_list)))
        if left:
            left_char_len = len(left_list[0])
        else:
            left_char_len = 0
        if right:
            right_char_len = len(right_list[0])
        else:
            right_char_len = 0
        out = ' ' * left_char_len
        out += value
        out += ' ' * right_char_len
        out += '\n'
        for i in range(lines):
            if i <= len(left_list) - 1:
                out += left_list[i]
            else:
                out += ' ' * left_char_len
            out += ' ' * value_char_len
            if i <= len(right_list) - 1:
                out += right_list[i]
            else:
                out += ' ' * right_char_len
            out += '\n'
        out = out[:-1]
        if not self.parent:
            newout = ''
            outlist = out.split('\n')
            for i in range(len(outlist)):
                newout += '%3d: %s\n' % (i, outlist[i])
            out = newout
        return out

seed = random.randint(r_min, r_max)
ele_list.append(seed)
a = BinTree(seed)

b = [random.randint(r_min, r_max) for i in range(eles - 1)]
for i in b:
    ele_list.append(i)
    a.add(i)

print ele_list
print a
