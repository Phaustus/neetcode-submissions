class Solution:
    def isValid(self, s: str) -> bool:
        r = []

        if s == []:
            return True
        if s[0] == ")" or s[0] == "]" or s[0] == "}":
            return False

        for i in s:
            if i == "(" or i == "[" or i == "{":
                r.append(i)
            elif r != []:
                if i == ")":
                    if r[-1] == "(":
                        r.pop()
                    else:
                        return False
                elif i == "]":
                    if r[-1] == "[":
                        r.pop()
                    else:
                        return False
                elif i == "}":
                    if r[-1] == "{":
                        r.pop()
                    else:
                        return False
            else:
                return False
        if r == []:
            return True
        else:
            return False

