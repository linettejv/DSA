class Solution:
    def isPalindrome(self, s: str) -> bool:
        # make the character list, remove the special characters. 
        char_list = [char.lower() for char in s if char.isalnum()]
        print(char_list)

        l = 0
        r = len(char_list) - 1
        while l < r:
            if char_list[l] != char_list[r]:
                return False
            l += 1
            r -= 1
        return True        

        

    # Notes : Fairly easy two pointer system
    # mistakes made : not including caps
    # take care to handle : numbers and avoid all other characters
    