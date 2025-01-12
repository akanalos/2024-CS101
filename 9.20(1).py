while True:
    try:
        ead=input()
    except EOFError:
        break
    check = list(ead)
    a1, a2, a3, a4 = 0, 1, 0, 1
    if check.count('@') == 1:
        a1 = 1
    if ('.@' in ead) or ('@.' in ead):
        a2 = 0
    if '@' in ead:
        loc = check.index('@')#如果没有这一元素，index会卡死
        if '.' in check[loc:]:
            a3 = 1
    if (check[0] == ('.' or '@')) or (check[-1] == ('.' or '@')):
        a4 = 0
    if all([a1, a2, a3, a4]):
        print('YES')
    else:
        print('NO')