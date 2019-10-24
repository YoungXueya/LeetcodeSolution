class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts=[0]*26
        for letter in magazine:
            
            counts[ord(letter)-ord('a')]+=1
    
        for letter in ransomNote:
            counts[ord(letter)-ord('a')]-=1
            if counts[ord(letter)-ord('a')]<0:
                return False
        
        return True
        
        
