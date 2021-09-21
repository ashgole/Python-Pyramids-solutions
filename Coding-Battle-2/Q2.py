"""
Q. 2

Program:
print:
            
12345
1234
123
12
1                                
    and so on...
    input: integer
"""

def solution(n):                                        #  definig function
                         
    try:                                                # Exception handling definig function
        #n=int(input("Enter No. of Rows: "))            # input
        n=5
        pc=1
        for x in range(6,1,-1):
            for y in range(1,x):
                print(y,end="")
            print()

    except:
        print("========== Error Occured ===========")   

if __name__ == "__main__":                              #Testcase
    n=5
    output=solution(n)