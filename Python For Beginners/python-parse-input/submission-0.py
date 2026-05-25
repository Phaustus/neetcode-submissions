from typing import List

def read_integers() -> List[int]:
    a = input()
    l = [int(x) for x in a.split(",")]
    return l

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
