"""
Q. 1

Program:
print:
            
        1
      2 3 2
    3 4 5 4 3
  4 5 6 7 6 5 4
5 6 7 8 9 8 7 6 5                              
    and so on...
    input: integer
"""

def solution(n):                                        #  definig function
                         
    try:                                                # Exception handling definig function
        #n=int(input("Enter No. of Rows: "))            # input
        n=5
        pc=1
        for x in range(1,n+1):
            for y in range(n-1,x-1,-1):
                print(" ",end=" ")
            for z in range(x-1,-x,-1):
                print(pc-abs(z),end=" ")
            pc+=2
            print()

    except:
        print("========== Error Occured ===========")   

if __name__ == "__main__":                              #Testcase
    n=5
    output=solution(n)