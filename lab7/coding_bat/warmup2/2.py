def string_splosion(str):
  ans_str = ""
  
  for i in range(0, len(str) + 1):
    ans_str += str[:i]
  
  return ans_str
