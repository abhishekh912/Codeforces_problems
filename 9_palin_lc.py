class Solution:
    def isPalindrome(self, x):
        # Convert the integer to a string
        x_str = str(x)
        # check if the string is equal to its reverse
        if x_str == x_str[::-1]:
            return True
        else:
            return False