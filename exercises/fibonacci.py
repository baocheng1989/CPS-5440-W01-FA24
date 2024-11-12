# bottom-up fibonnaci
def fib(n:int)->int:
    if n==0:
        return 0
    if n==1:
        return 1
    fi,f1,f2=1,0,1
    for i in range(2,n+1):
        # fi,f1,f2=f1+f2,f2,fi
        fi=f1+f2
        f1=f2
        f2=fi
    return fi

if __name__=='__main__':
    # print(fib(3))
    for i in range(11):
        print(fib(i))