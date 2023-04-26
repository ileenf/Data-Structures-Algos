class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combos = set()

        def create_combo(candidates, path, total):
            if total == 0:
                combos.add(tuple(sorted(path)))
            elif total < 0:
                return
            else:
                for num in candidates:
                    create_combo(candidates, path + [num], total - num)

        
        create_combo(candidates, [], target)
        return combos
            
