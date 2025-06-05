class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        
        n=len(word)-numFriends+1
        max_substring=" "

        if numFriends==1:
            return word

        for i in range(0,len(word)+1):
            current = word[i:i+n]
            if current > max_substring:
                max_substring = current 

        return max_substring




        
