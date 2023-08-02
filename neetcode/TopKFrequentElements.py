class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mydict = defaultdict(lambda:0)
        for num in nums:
            mydict[num] +=1

        occurence = [[] for _ in range(len(nums)+1)]

        for key,value in mydict.items():
            occurence[value].append(key)

        result = []
        i = len(occurence) - 1

        while k>0:
            if k > len(occurence[i]):
                result += occurence[i]
            else:
                result += occurence[i][:k]
            k -= len(occurence[i])
            i -= 1
        
        return result