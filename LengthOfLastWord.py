class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        flag = False
        cnt = 0
        for i in range(-1, - len(s) - 1, -1):
            if s[i] == " " and flag == False:
                continue
            if s[i] != " ":
                flag = True
                cnt += 1
            else:
                break
        return cnt

    def SplitMethod(self, s: str) -> int:
        array = s.split()
        return len(array[-1])

    def whileLoop(self, s: str) -> int:
        cnt = 0
        i = len(s) - 1
        while i >= 0 and s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            cnt += 1
            i -= 1
        return cnt

ans = Solution()
abc = ans.whileLoop("a")

print(abc)