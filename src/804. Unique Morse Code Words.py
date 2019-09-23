class Solution:
    #Better performance
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        dic={"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
        converted=set()
        for word in words:
            
            cur=[dic[char] for char in word]
            
            cur="".join(cur)
            if cur not in converted:
                converted.add(cur)
         
        return len(converted)
 
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        dic=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        converted=set()
        for word in words:
            cur=[dic[ord(char)-ord('a')] for char in word]
            cur="".join(cur)
            if cur not in converted:
                converted.add(cur)
        return len(converted)
                
