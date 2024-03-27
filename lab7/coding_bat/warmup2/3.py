def array_front9(nums):
  ln = 4
  if len(nums) < 4:
    ln = len(nums)

  for i in range(0, ln):
    if nums[i] == 9:
      return True
  
  return False