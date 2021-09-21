"""
Q. 1

Program:
print:
         *
       *   *
     *   *   *
   *   *   *   *
 *   *   *   *   *
 *   *   *   *   *
   *   *   *   *
     *   *   *
       *   *
         *
               
    and so on...
    input: integer
"""
def star(n):                           # Defining function
    try:                                    # Exception Handling
        # n= int(input ("Enter n value: "))
        
        for i in range(n+1):
            for k in range(n,i,-1):
                print(' ',end=" ")
            for k in range(i,0,-1):
                print(' * ',end=" ")
            print()
        for i in range(n,0,-1):
            for k in range(n,i,-1):
                print(' ',end=" ")
            for k in range(i,0,-1):
                print(' * ',end=" ")
            print()


    except:
            print("========== Error Occured ===========") 

if __name__ == "__main__":                              # Testcase
    
    star(5)