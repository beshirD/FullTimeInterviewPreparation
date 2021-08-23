class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_letters = {}
        visited = set()
        for i in range(len(s)):
            if s[i] in map_letters:
                if map_letters[s[i]] != t[i]:
                    return False
            else:
                if t[i] not in visited:
                    visited.add(t[i])
                    map_letters[s[i]] = t[i]
                else:
                    return False
        return True