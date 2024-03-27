def front_back(str):
  if len(str) <= 1:
    return str
  
  str = list(str)
  str[0], str[-1] = str[-1], str[0]

  return ''.join(str)
