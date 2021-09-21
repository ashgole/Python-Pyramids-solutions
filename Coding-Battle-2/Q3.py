"""
Q. 3

Program:
print:
1
1 2
1   3
1     4
1 2 3 4 5          
                                 
    and so on...
    input: integer
"""

def solution(n):                                         #  definig function
    try:                                                # Exception handling definig function

         #n=int(input("Enter No. of Rows: "))            # input
         
        for c in range(1, n+1):
            for r in range(1, n+1):
                if (c==n) or (r==1) or (r==c):
                    print(r, end=" ")
                else:
                    print(" ", end=" ")
            print()
    except:
        print("========== Error Occured ===========")   

if __name__ == "__main__":                              #Testcase
    n=5
    output=solution(n)