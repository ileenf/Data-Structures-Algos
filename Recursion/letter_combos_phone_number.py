class Solution:
    def __init__(self):
        self.mappings = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
    def letterCombinations(self, digits: str) -> List[str]:
        def get_combos(digits, combo, all_combos):
            if not digits:
                return all_combos.append(combo)

            digit = digits[0]
            for letter in self.mappings[digit]:
                get_combos(digits[1:], combo + letter, all_combos)

        all_combos = []
        get_combos(digits, '', all_combos)
        return all_combos
