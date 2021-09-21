"""
Q. 2

Program:
print:

1
2* 3
4* 5* 6
7* 8* 9* 10
7* 8* 9* 10
4* 5* 6
2* 3
1

    and so on...
    input: integer
"""
def solution(n):                # defining function
    try:                       # exception handling
        j=1
        for i in range(1,n+1):
            print(" ".join(str(x)+'*' for x in range(j,j+i))[:-1])
            j=j+i
        for i in range(n,0,-1):
            print(" ".join(str(x)+'*' for x in range(j-i,j))[:-1])
            j=j-i
    except:
            print("========== Error Occured ===========")

if __name__ == "__main__":                              # Testcase
    solution(4)