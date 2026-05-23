class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_sorted = [''.join(sorted(w)) for w in strs]
        
        m = {}
        r = []

        for i, val in enumerate(char_sorted):
            if val in m:
                m[val].append(i)
            else:
                m[val] = [i]
                
        for key in m:
            r.append([strs[i] for i in m[key]])

        return r

