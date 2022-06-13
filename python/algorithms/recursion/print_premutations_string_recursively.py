# Python program to print all permutations with 
# duplicates allowed 
  
def toString(List): 
    return ''.join(List) 
  
# Function to print permutations of string 
# This function takes three parameters: 
# 1. String 
# 2. Starting index of the string 
# 3. Ending index of the string. 
def permute(a, n, l=0): 
    if l==n: 
        print (toString(a))
    else: 
        for i in range(l,n): 
            a[l], a[i] = a[i], a[l] 
            permute(a, n, l+1) 
            a[l], a[i] = a[i], a[l] # backtrack 

def main():
    a = list(input('Enter a string: '))
    n = len(a)
    permute(a, n)

if __name__ == "__main__":
    main()