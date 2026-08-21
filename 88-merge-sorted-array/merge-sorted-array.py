class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        s = []
        for i in range(m):
           s.append(nums1[i])
        for i in range(n):
            s.append(nums2[i])
        s.sort()  
        for i in range(len(s)):
            nums1[i] = s[i]