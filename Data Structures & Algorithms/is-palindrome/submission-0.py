class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean = ""
        rev = ""

        for i in s:
            if i.isalnum():
                clean = clean + i.lower()

        for j in clean:
            rev = j + rev

        if rev == clean:
            return True
        else:
            return False

        