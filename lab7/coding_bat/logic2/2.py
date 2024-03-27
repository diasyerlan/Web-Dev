def no_teen_sum(a, b, c):
  if a >= 13 and a <= 19:
    if a != 15 and a != 16:
      a = 0
  if b >= 13 and b <= 19:
    if b != 15 and b != 16:
      b = 0
  if c >= 13 and c <= 19:
    if c != 15 and c != 16:
      c = 0
      
  return a + b + c