# -*- coding: utf-8 -*-
def triangles():
    s = [1]
    yield s
    while (1):
        if len(s) == 1:
            re = [1, 1]
            s = re
            yield re
        re = [1]
        for x in range(len(s)-1):
            re.append(s[x]+s[x+1])
        re.append(1)
        s = re
        yield re

g = triangles()
print(next(g))
print(next(g))
print(next(g))