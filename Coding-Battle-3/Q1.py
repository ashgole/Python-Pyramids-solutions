"""
Q. 1

Program:
print:
1
1 2 1
1 2 3 2 1
1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
               
    and so on...
    input: integer
"""


def solution(i):                            # Defining function
    try:                                     # Exception Handling
        for x in range(1,i+2):
            for y in range(1,x-1):
                print(y,end=" ")
            for y in range(x-1,0,-1):
                print(y,end=" ")
            print()
    except:
        print("========== Error Occured ===========") 

if __name__ == "__main__":                              # Testcase
    
    i= 5
    solution(i)