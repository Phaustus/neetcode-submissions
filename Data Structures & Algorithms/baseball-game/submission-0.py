class Solution:
    def calPoints(self, operations: List[str]) -> int:
        r = []
        for i, val in enumerate(operations):
            if val != "C" and val != "+" and val != "D":
                r.append(int(val))
            elif val == "+":
                r.append(int(r[-1]) + int(r[-2]))
            elif val == "C":
                r.pop()
            elif val == "D":
                h = 2 * int(r[-1])
                r.append(h)

        rez = 0
        for i in r:
            rez += int(i)

        return rez