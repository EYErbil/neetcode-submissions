class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Map frequencies
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        # 2. Create buckets where index = frequency
        freq_buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            freq_buckets[freq].append(num)
            
        # 3. Traverse backwards to grab the top K
        result = []
        for i in range(len(freq_buckets) - 1, 0, -1):
            for num in freq_buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

        

        


        




