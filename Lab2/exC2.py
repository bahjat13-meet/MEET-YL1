from random import randint
def Q2():
    if randint(0,2)==1:
        return "H"
    else:
        return "T"
if __name__=="__main__":
    while True:
        x=raw_input()
        if(x=="n"):
            print Q2()
