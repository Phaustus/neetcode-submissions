from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    m = {}
    for i,in word:
        if i in m:
            m[i] += 1
        else:
            m[i] = 1
    return m




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
