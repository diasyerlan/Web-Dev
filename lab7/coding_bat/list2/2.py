def sum13(nums):
  sum = 0
  ok = True
  for i in nums:
    if i == 13:
      ok = False
      continue
    if ok:
      sum += i
    else:
      ok = True
  
  return sum
