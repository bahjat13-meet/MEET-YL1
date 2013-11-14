def isPolindrome(n):
    for i in range(0,((len(n)-1)/2)):
        if n[i]!=n[len(n)-1-i]:
            return False
    return True
