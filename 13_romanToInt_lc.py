class Solution(object):
    def romanToInt(self, s):
        def check(r):
            if r == "I":
                return 1
            elif r == "V":
                return 5
            elif r == "X":
                return 10
            elif r == "L":
                return 50
            elif r == "C":
                return 100
            elif r == "D":
                return 500
            elif r == "M":
                return 1000
            else:
                return 0

        sum1 = 0
        prev_value = 0

        for i in s[::-1]:
            current_value = check(i)
            if current_value >= prev_value:
                sum1 += current_value
            else:
                sum1 -= current_value
            prev_value = current_value

        return sum1
