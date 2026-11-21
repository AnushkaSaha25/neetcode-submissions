class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_contains = defaultdict(int)
        for char in s:
            s_contains[char] += 1

        t_contains = defaultdict(int)
        for char in t:
            t_contains[char] += 1

        return s_contains == t_contains

        
        
        