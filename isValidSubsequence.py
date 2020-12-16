#Validate Subsequence

def isValidSubsequence(array, sequence):
    if len(array) <  len(sequence):
         return False
    if len(sequence) == 0:
            return True
    idx = 0
    while len(array) != 0:
        if idx == array.pop(0):
            idx+=1
    return idx == len(sequence) 

            

            
            


        
    pass
