import math
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #1. 띄어쓰기 없이 짝수인지 체크 O(n)
        char_cnt = 0
        char_alpha_list = []
        for char in range(len(s)):
            if s[char].isalnum():
                char_cnt += 1
                lower_case = s[char].lower()
                char_alpha_list.append(lower_case)
            else:
                continue

        #1.1 혹시 문자가 두개나 하나면
        if len(char_alpha_list) == 1:
            return True
        elif len(char_alpha_list) == 2:
            if char_alpha_list[0] != char_alpha_list[1]:
                return False
            return True
        elif len(char_alpha_list) == 0:
            return True


        #2.1 짝수면? 1/2해서 순회
        if char_cnt % 2 == 0:
            for i in range(int(len(char_alpha_list) / 2)):
                back_i = (len(char_alpha_list) - 1) - i
                if char_alpha_list[i] != char_alpha_list[back_i]:
                    return False
            return True

        #2.2 짝수가 아니면? 1/2하고 소수점 날리기
        else:
            for j in range(int(len(char_alpha_list) / 2)):
                back_j = (len(char_alpha_list) - 1) - j
                if char_alpha_list[j] != char_alpha_list[back_j]:
                    return False
            return True
