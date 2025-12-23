class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []

        for x, y in points:
            distance = (x**2 + y**2) ** 0.5
            distances.append(([x, y], distance))

        sorted_distances = sorted(distances, key=lambda x: x[1])
        return [point[0] for point in sorted_distances][:k]


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []

        heapq.heapify(distances)

        for x, y in points:
            distance = (x**2 + y**2) ** 0.5
            heapq.heappush(distances, [distance, [x, y]])

        points = []
        for _ in range(k):
            distance, point = heapq.heappop(distances)
            points.append(point)
        
        return points
