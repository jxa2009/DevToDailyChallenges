# The Deaf Rats of Hamelin - 136
# Story
# The Pied Piper has been enlisted to play his magical tune and coax all the rats out of town.

# But some of the rats are deaf and are going the wrong way!

# How many deaf rats are there?

# Legend
#     P = The Pied Piper
#     O~ = Rat going left
#     ~O = Rat going Right

# Example
#     ex1 ~O~O~O~O P has 0 deaf rats
#     ex2 P O~ O~ ~O O~ has 1 defa rats
#     ex3 ~O~O~O~OP~O~OO~ has 2 deaf rats

class Solution(object):
        
    # When this function returns:
    #   0: the rat is going left
    #   1: the rat is going right
    def ratDirection(self,rat):
        if rat[0] == "~": #going right
            return 1
        return 0 # going left
    
    # Direction:
    #   1 for right
    #   -1 for left
    def ratParser(self,rats):
        ratDirections = [0,0]
        index = 0
        while index < len(rats):
            rat = rats[index] + rats[index+1]
            if self.ratDirection(rat): #going right
                ratDirections[1] += 1
            else: # going left
                ratDirections[0] += 1
            index += 2
        return ratDirections



    def numDeafRats(self,string):
        # Remove the white space and split based on where the "Pied Piper" is
        rats= [x.replace(" ","") for x in string.split('P')] 
        leftRats= rats[0]
        rightRats =rats[1]

        deafRats = 0
        
        # Num rats going left that should be going right
        deafRats += self.ratParser(leftRats)[0]

        # Num rats going right that should be going left
        deafRats += self.ratParser(rightRats)[1]
        
        return deafRats

def main():
    ex1 = "~O~O~O~O P"
    ex2 = "P O~ O~ ~O O~"
    ex3 = "~O~O~O~OP~O~OO~"
    arr = [ex1,ex2,ex3]
    ratsObj = Solution()

    for item in arr:
        print(ratsObj.numDeafRats(item))
main()    
    
            



