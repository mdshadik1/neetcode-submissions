class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean="" #taking a empty string
        for i in s:
            if i.isalnum(): #here checking and removing extra thing 
                clean +=i.lower()
        
        return clean == clean[::-1]