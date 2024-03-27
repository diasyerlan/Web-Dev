def caught_speeding(speed, is_birthday):
  if is_birthday:
    if speed >= 86:
      return 2
    elif speed >= 66:
      return 1
    else:
      return 0
  
  if speed >= 81:
    return 2
  elif speed >= 61:
    return 1
  return 0
