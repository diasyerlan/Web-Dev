def make_chocolate(small, big, goal):

    big_needed = min(big, goal // 5)

    remaining = goal - (big_needed * 5)
    
    small_needed = min(remaining, small)
    

    if small_needed + (big_needed * 5) == goal:
        return small_needed
    
    return -1