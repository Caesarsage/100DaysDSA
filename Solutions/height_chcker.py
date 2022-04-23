class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        count = 0
        expected = sorted(heights)
        
        for num in range(len(heights)):
            if heights[num] != expected[num]:
                count+=1
        return count

# class Solution:
#     def heightChecker(self, heights: List[int]) -> int:
#         max_nr = max(heights)
#         # initialize frequency array with 0's
#         count = [0] * (max_nr + 1)
#         # get frequencies
#         for number in heights:
#             count[number] += 1
#         # create a sumcount array
#         sumcount = [0] * (max_nr + 1)
#         for index, number in enumerate(count[1:],start=1):
#             sumcount[index] = number + sumcount[index-1]
#         # sumcount determines the index in sorted array
#         # create output array
#         output = [0] * len(heights)
#         # loop backwards starting with last element for stable sort
#         for p in range(len(heights)-1,-1,-1):
#             output[sumcount[heights[p]]-1] = heights[p]
#             sumcount[heights[p]] -= 1
# 		# return the difference compared to original array
#         result = 0
#         for index, number in enumerate(heights):
#             if number != output[index]:
#                 result += 1
#         return result