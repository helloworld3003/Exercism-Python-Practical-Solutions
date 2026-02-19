def score(x, y):
    dis=(x**2+y**2)**0.5
    if dis<=1: return 10
    elif dis<=5: return 5
    elif dis<=10: return 1
    else: return 0
