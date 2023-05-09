class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combos = []

        def generate(left_count, right_count, path):
            if left_count == right_count and left_count == n:
                combos.append(path)
                return
            if left_count < n:
                generate(left_count + 1, right_count, path + '(')
            if right_count < left_count:
                generate(left_count, right_count + 1, path + ')')

        generate(0, 0, '')
        return combos
