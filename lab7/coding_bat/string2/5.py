def cat_dog(str):
    cnt_dog = 0
    cnt_cat = 0
    
    for i in range(len(str) - 1):
        if str[i:i + 3] == 'cat':
            cnt_cat += 1
        if str[i:i + 3] == 'dog':
            cnt_dog += 1
    return cnt_cat == cnt_dog


