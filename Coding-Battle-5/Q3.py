"""
Q. 3

Program:
print:
*
*1*
*121*
*12321*
*121*
*1*
*

    and so on...
    input: integer
"""
def solution(n):
    num=1
        # outer loop upper part
    print("*")
    for row in range(1,n+1):
                # inner loop to handle number column
        print("*", end="")
        for col in range(1,row+1):
            print(col, end="")
        for col in range(col-1, 0, -1):
            print(col, end="")
        num=num+1
        print("*")

    for row in range(n-1,0,-1):  #for lower part reverse direction
        print("*", end="")
        for col in range(1,row+1):
            print(col, end="")
        for col in range(col-1, 0, -1):
            print(col, end="")

        print("*")
    print("*")
if __name__=="__main__":
    try:
        n=int(input("Please Enter the desired number of rows:"))
        if n>0:
            solution(n)
        else:
            print("Please enter a Positive Integer:")
    except:
        print("Opps,Invalid input.")