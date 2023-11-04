class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if left==[] and right!=[]:
            return n-min(right)
        elif left!=[] and right==[]:
            return max(left)
        
        leftmost=min(right)
        rightmost=max(left)
        leftleast=max(right)
        rightleast=min(left)
        
        return max(rightmost,n-leftmost)

