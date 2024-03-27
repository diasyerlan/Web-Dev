def front3(str):
  ln = 3
  if len(str) <  ln:
    ln = len(str)
    
  ans = str[:ln]
  
  return ans * 3
