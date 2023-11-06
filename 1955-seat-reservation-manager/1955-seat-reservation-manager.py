from bisect import insort
class SeatManager:
    lst=[]
    def __init__(self, n: int):
        self.lst=[i for i in range(1,n+1)]

    def reserve(self) -> int:
        return self.lst.pop(0)
        

    def unreserve(self, seatNumber: int) -> None:
        insort(self.lst,seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)