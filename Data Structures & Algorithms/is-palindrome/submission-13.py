class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            #레프트 불통과 조건
            if not s[left].isalnum():
                left += 1
                continue
            #라이트 불통과 조건
            if not s[right].isalnum():
                right -= 1
                continue
            #다를때
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
