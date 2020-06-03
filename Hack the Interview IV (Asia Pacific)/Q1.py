
def minimumMoves(s, d):
    c=0
    ss=s.split("1")
    for i in ss:
        c+=len(i)//d
    return(c)
