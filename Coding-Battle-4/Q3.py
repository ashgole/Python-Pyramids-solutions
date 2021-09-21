"""
Q. 3

Program:
print:
 *
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
               
    and so on...
    input: integer
"""
def solution(n):                            # Defining function
    try:                                    # Exception Handling
        size=5
        for x in range(size,-(size),-1):
            for y in range(1,abs(x)+1):
                print("",end="")
            for z in range(size,abs(x),-1):
                print("* ",end="")
            print()
    except:
            print("========== Error Occured ===========")

if __name__ == "__main__":                              # Testcase

    n= 5
    solution(n)