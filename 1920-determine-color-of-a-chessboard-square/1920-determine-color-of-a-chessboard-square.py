class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        row=ord(coordinates[0])-ord('a')+1
        col=int(coordinates[1])
        return (row+col)%2!=0
        