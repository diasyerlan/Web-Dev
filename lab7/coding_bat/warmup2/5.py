def last2(str):
  if len(str) < 2:
    return 0
  
  end = str[len(str) - 2: ]
  cnt = 0
  
  for i in range(0, len(str) - 2):
    if str[i: i + 2] == end:
      cnt += 1

  return cnt