class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        if len(s2)<len(s1) or len(s1)==0:
            return False
        count = Counter(s1)
        freq_window = {}
        l=0
        
        for r in range(len(s2)):
            freq_window[s2[r]] = 1+ freq_window.get(s2[r],0)
            while(r-l+1>length):
                freq_window[s2[l]]-=1
                if (freq_window[s2[l]]==0):
                    del freq_window[s2[l]]
                l+=1
            if (count == freq_window):
                return True
        return False

        