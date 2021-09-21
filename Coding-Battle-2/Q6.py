"""
Q. 6

Program:
print:
1 2 3 4 5 
2     5 
3   5 
4 5 
5          
                                 
    and so on...
    input: integer
"""
def solution(n):                                        #  defining function
    try:                                                # Exception handling definig function
        #n=int(input("Enter No. of Rows: "))            # input

        for r in range(1, n+1):
                    for c in range(r, n+1):
                        if (c==n) or (r==1) or (r==c):
                            print(c , end=" ")
                        else:
                            print(" " , end=" ")
                    print()
    except:
        print("========== Error Occured ===========")   
    
if __name__ == "__main__":                              #Testcase
    n=5
    output=solution(n)