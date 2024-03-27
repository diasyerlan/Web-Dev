def front_times(str, n):
  ln = 3
  if len(str) <  ln:
    ln = len(str)
    
  ans = str[:ln]
  
  return ans * n

