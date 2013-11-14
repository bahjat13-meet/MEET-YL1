from random import randint
def Q2():
    if randint(0,2)==1:
        return "H"
    else:
        return "T"
def Q4(times):
    l=[]
    for i in range(0,times):
        l.append(Q2())
    return l
if __name__=="__main__":
    t=int(raw_input())
    print Q4(t)
