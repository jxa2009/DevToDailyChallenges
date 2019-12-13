# Create a  function that removes the first and last letters of a string
# Strings with two characters or less are considered invalid.
# Function can choose to return null or ignore in this case
class Solution(object):
    def peeler(self,string):
        if len(string) <= 2:
            return None
        return string[1:len(string)-1]

def main():
    arr = ["123","1","hi","Hello World", "", "Cool"]
    peel = Solution()
    for item in arr:
        print("Unpeeled: "+ item , "Peeled: ", peel.peeler(item))
main()