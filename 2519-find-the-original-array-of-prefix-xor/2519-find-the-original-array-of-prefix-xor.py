class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        lst=[0]*len(pref)
        lst[0]=pref[0]
        for i in range(1,len(pref)):
            lst[i]=pref[i]^pref[i-1]
        return lst