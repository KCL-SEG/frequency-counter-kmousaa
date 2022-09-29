"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}

    for i in items:
        x = str(i)
        if x != frequencies:
            frequencies[x] = 0

        else:
            frequencies[x] += 1

    return frequencies
