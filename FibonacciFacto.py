if __name__ == '__main__':
    a,b = 0,1
    flist = []
    for i in range(0,9):
        print(a,end=' ')
        flist.append(a)
        a,b = b,a+b
    print()
    print(flist)

    def facto(n):
        fact = 1
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            for i in range(n,0,-1):
                fact = fact * i
            return fact
    print("FACTORIALs of above Series :==> ")
    print(list(map(facto, flist)))
    #print("Factorial of 8 : ", facto(8))
    print("SQUAREs of Numbers in above series :=> ")
    print(list(map(lambda x : x*x,flist)))
    print("CUBEs of the numbers in the above List :=> ")
    print(list(map(lambda x :x**3, flist)))
