"""Frequencies function."""

def frequencies(items):
    frequencies = {}

    for i in items:
        x = str(i)
        if x in frequencies:
          frequencies[x] += 1

        else:
            frequencies[x] = 1
            print(x , "is new!")

    return frequencies
