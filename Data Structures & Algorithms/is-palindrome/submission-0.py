import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove spaces and reverse the string and compare
        cleaned = re.sub(r'[^A-Za-z0-9]','',s)
        cleaned = cleaned.lower()
        # s_no_space = cleaned.replace(" ","")
        print(cleaned[::-1])
        return cleaned == cleaned[::-1]
        