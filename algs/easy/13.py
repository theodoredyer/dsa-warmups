class Solution:
    def romanToInt(self, s: str) -> int:
        value_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        string_arr = list(s)
        total_value = 0
        for elem in string_arr:
            total_value += value_map[elem]

        for i in range(len(string_arr) - 1):
            if value_map[string_arr[i]] < value_map[string_arr[i + 1]]:
                total_value -= 2 * value_map[string_arr[i]]

        return total_value
