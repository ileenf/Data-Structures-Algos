class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def perform_division(var1, var2, val, neighbors):
            if var1 == var2:
                return val
            seen.add(var1)
            
            for neighbor, div_value in neighbors[var1]:
                if neighbor not in seen:
                    result = perform_division(neighbor, var2, val * div_value, neighbors)
                    if result != -1:
                        return result
            return -1
        neighbors = defaultdict(list)

        for i in range(len(equations)):
            var1, var2 = equations[i]
            value = values[i]
            
            neighbors[var1].append([var2, value])
            neighbors[var2].append([var1, 1/value])
        query_result = []
        for query in queries:
            var1, var2 = query
            if var1 not in neighbors or var2 not in neighbors:
                query_result.append(-1)
            else:
                seen = set()
                result = perform_division(var1, var2, 1, neighbors)
                query_result.append(result)
            
        return query_result
