def make_ends(nums):
  if len(nums) < 1:
    return nums
  
  arr = [nums[0], nums[-1]]
  return arr
