"""
Q. 1

Program:
print:
*****1*****
****2*2****
***3*3*3***
**4*4*4*4**
*5*5*5*5*5*     
               
    and so on...
    input: integer
"""


def solution(n):                            # Defining function
    try:                                    # Exception Handling
        for i in range(n):
            print("*"*(n-i)+(str(i+1)+"*")*(i+1)+"*"*(n-i-1))
    except:
        print("========== Error Occured ===========") 

if __name__ == "__main__":                              # Testcase
    
    n= 5
    solution(n)