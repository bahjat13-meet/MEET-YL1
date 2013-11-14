if __name__=="__main__":
    dict={}
    for i in range(0,3):
        print "Enter name :"
        n=raw_input()
        print "Enter age :"
        a=int(raw_input())
        dict[n]=a
    print dict
