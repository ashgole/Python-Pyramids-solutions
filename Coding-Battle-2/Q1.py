"""
Q. 1

Program:
print:
            
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5                                 
    and so on...
    input: integer
"""

def solution(n):                                        #  definig function
                         
    try:                                                # Exception handling definig function
        #n=int(input("Enter No. of Rows: "))            # input
        for i in range(n+1):
            for j in range(1, i+1):
                print(j, end=" ")
            print()
        return n

    except:
        print("========== Error Occured ===========")   

if __name__ == "__main__":                              #Testcase
    n=5
    output=solution(n)