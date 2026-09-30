class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        if(len(s) != len(t)):
            return False
        for letter in s:
            if letter not in freq:
                freq[letter] = 0
            freq[letter] += 1
        
        for letter in t:
            if letter not in freq:
                return False
            freq[letter] -= 1

            if freq[letter] < 0:
                return False

        return True
