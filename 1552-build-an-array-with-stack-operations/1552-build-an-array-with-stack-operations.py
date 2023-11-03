class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack=[]
        for i in range(1,max(target)+1):
            if i not in target:
                stack.append("Push")
                stack.append("Pop")
            else:
                stack.append("Push")
        return stack