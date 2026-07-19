import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # # remove spaces and reverse the string and compare
        # cleaned = re.sub(r'[^A-Za-z0-9]','',s)
        # cleaned = cleaned.lower()
        # # s_no_space = cleaned.replace(" ","")
        # print(cleaned[::-1])
        # return cleaned == cleaned[::-1]
        i,j = 0,len(s)-1
        while i <j:
            while i<j and not s[i].isalnum():
                i+=1
            while i<j and not s[j].isalnum():
                j-=1
            if s[i].lower() != s[j].lower():
                return False
            i+=1
            j-=1
        return True
        