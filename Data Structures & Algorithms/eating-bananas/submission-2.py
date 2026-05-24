class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        min_mid = float('inf')

        def check(n: int, piles: list[int], h: int, min_mid):
            cnt = 0
            for i in piles:
                cnt += math.ceil(i / n)
            
            if cnt > h:
                #nedovoljno vremena
                return -1
            elif cnt <= h:
                #previse vremena
                return 1

        i = 1
        j = max(piles)

        while i <= j:
            mid = (i + j) // 2
            match check(mid, piles, h, min_mid):
                #kad je i dalje nedovoljno vremena, idi na vece cifre
                case -1:
                    i = mid + 1
                #kad je i dalje vise nego dovoljno vremena, idi na manje cifre
                case 1:
                    j = mid - 1
                    if min_mid > mid:
                        min_mid = mid
                
        if min_mid != float('inf'):
            return int(min_mid)
        return -1