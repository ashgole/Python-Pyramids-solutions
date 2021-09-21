"""
Q. 2

Program:
print:
       
    1
   121
  12321
 1234321
123454321             
    and so on...
    input: integer
"""


def solution(n):                            # Defining function
    try:                                    # Exception Handling
        for x in range(1,n+1):
            for y in range(n,x,-1):
                print(" ",end=" ")
            for z in range(x-1,-x,-1):
                print(x-abs(z),end=" ")
            print()
        
        """                                 
        for r in range (1,n+1):

            for s in range(n,r, -1):        
                print(" ", end= "")

            for c in range (1, r+1):
                print(c, end= "") 

            for c in range(c-1, 0, -1):
                print(c, end="")

            print()
        """
            
           
    except:
        print("========== Error Occured ===========") 

if __name__ == "__main__":                              # Testcase
    
    n= 5
    solution(n)
    
   