import random

def mergeFunc(px, py, v1, v2):
    # Red, Green & Blue
    v1r, v1g, v1b = v1[0], v1[1], v1[2]
    v2r, v2g, v2b = v2[0], v2[1], v2[2]
    r, g, b = 0, 0, 0
    # Insert logic here:
    k = min(max((px - 512) / 100 + 0.5, 0), 1)
    r = v1r + (v2r - v1r) * k
    g = v1g + (v2g - v1g) * k
    b = v1b + (v2b - v1b) * k
    # value is between 0 - 1, 0 = v1, 1 = v2, and in between blends them together.
    return [r, g, b]