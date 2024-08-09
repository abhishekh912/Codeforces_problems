# It's leet code program
class Solution(object):
    def twoSum(self, nums, target):
        # Create a dictionary to store the complement and its index
        num_to_index = {}
        
        # Iterate through the list of numbers
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                # If the complement is found, return the indices
                return [num_to_index[complement], index]
            num_to_index[num] = index
        
        # Return None if no solution is found
        return None

# Input the list of numbers
nums = list(map(int, input().split()))

# Validate the length of nums
if not 2 <= len(nums) <= 10**4:
    exit()

# Validate the range of each number in nums
for num in nums:
    if not -10**9 <= num <= 10**9:
        exit()

# Input the target value
target = int(input())
if not -10**9 <= target <= 10**9:
    exit()

# Instantiate the Solution class and call twoSum
solution = Solution()
result = solution.twoSum(nums, target)

# Print the result
if result:
    print(result)
else:
    print("No two sum solution")
