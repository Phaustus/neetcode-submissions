import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    heap = []
    for num in nums:
        # Use the negative of the number as the priority to simulate a max heap
        heapq.heappush(heap, (-num, num))
    
    result = []
    while heap:
        # Pop the tuple and take the original value
        priority, original_num = heapq.heappop(heap)
        result.append(original_num)
    return result



# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))