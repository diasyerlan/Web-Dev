def sum67(nums):
  sum = 0
  ok = True
  for i in nums:
    if i == 6:
      ok = False
      continue
    if ok:
      sum += i
    elif i == 7:
      ok = True
  
  return sum

