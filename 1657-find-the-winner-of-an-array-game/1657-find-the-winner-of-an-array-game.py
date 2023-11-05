class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        
        if k>=len(arr):
            return max(arr)

        count1=0
        count0=0

        while count1<k and count0<k:
            if arr[0]>arr[1]:
                val=arr.pop(1)
                arr.append(val)
                count0+=1
                count1=0
            else:
                val=arr.pop(0)
                arr.append(val)
                count1+=1
                count0=count1
                count1=0
            
        return arr[0]


        