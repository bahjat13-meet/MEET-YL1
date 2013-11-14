def Q3(probsH):
    if randint(0,101)<(probsH*100):
        return "H"
    else:
        return "T"
if __name__=="__main__":
    print ("Write the probability (0.00-1.00) :")
    probs=float(raw_input())
    while True:
        x=raw_input()
        if(x=="n"):
            print Q3(probs)
