#Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

nums, k  = [1,1,1,2,2,3,3,3], 2

from collections import Counter

def top_k_elements(nums, k):
  counts = Counter(nums)
  return [x[0] for x in counts.most_common(k)]


print(zip(top_k_elements(nums, k), range(k)))