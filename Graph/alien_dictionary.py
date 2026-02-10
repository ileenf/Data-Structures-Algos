class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indegrees = {ch: 0 for word in words for ch in word}

        for word1, word2 in zip(words, words[1:]):
            if word1.startswith(word2) and len(word2) < len(word1):
                return ''
            for ch1, ch2 in zip(word1, word2):
                if ch1 != ch2:
                    if ch2 not in graph[ch1]:
                        graph[ch1].add(ch2)
                        indegrees[ch2] += 1
                    break

        queue = deque([ch for ch in indegrees if indegrees[ch] == 0])
        order = []

        while queue:
            ch = queue.popleft()
            order.append(ch)

            for node in graph[ch]:
                indegrees[node] -= 1
                if indegrees[node] == 0:
                    queue.append(node)
       
        if len(order) != len(indegrees):
            return ''

        return ''.join(order)
