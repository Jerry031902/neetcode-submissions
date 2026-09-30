class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {};
        
        for num in nums:
            if num not in freq:
                freq[num] = 0
            
            freq[num]+=1
        
        sorted_by_value = sorted(freq.items(), key = lambda item: item[1], reverse = True)

        result = []

        for num, count in sorted_by_value[:k]:
            result.append(num)
        return result

        