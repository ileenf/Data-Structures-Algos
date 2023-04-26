class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        combos = set()

        def generate_combos(path, total, k, start):
            if total == 0 and len(path) == k:
                combos.add(tuple(sorted(path)))
            elif total < 0:
                return

            for num in range(start, 10):
                path.add(num)
                generate_combos(path, total - num, k, num+1)
                path.remove(num)
        
        generate_combos(set(), n, k, 1)
        return combos
