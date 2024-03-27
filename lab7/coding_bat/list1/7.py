def max_end3(nums):
  mx = 0
  if nums[0] > nums[2]:
    mx = nums[0]
  else:
    mx = nums[2]
  nums[0] = mx
  nums[1] = mx
  nums[2] = mx
  
  return nums
