def countApplesAndOranges(s, t, a, b, apples, oranges):
    app_cnt = 0
    org_cnt = 0
    for ap in apples:
        if ap > 0:
            if t >= a+ap >= s:
                app_cnt += 1
    for og in oranges:
        if og < 0:
            if t >= b+og >= s:
                org_cnt += 1
    print(app_cnt)
    print(org_cnt)
countApplesAndOranges(7, 11, 5, 15, [-2,2,1],[5,-6])    