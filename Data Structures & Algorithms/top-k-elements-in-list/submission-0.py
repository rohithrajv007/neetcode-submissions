class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash={}
        for num in nums:
            hash[num]=hash.get(num,0)+1
            def sort_key(x):
                return hash[x]
        return sorted(hash.keys(),key=sort_key,reverse=True)[:k]
        
        