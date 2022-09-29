class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        def manhattan_dist(x1, y1, x2, y2):
            return abs(x1-x2) + abs(y1-y2)
        
        distances = []
        
        for i, worker in enumerate(workers):
            for j, bike in enumerate(bikes):
                dist = manhattan_dist(worker[0], worker[1], bike[0], bike[1])
                distances.append([dist, i, j])
        
        sorted_distances = sorted(distances)
        
        worker_bike_pos = [-1 for _ in range(len(workers))]
        assigned_bikes = set()
        
        for dist, worker, bike in sorted_distances:
            if worker_bike_pos[worker] == -1 and bike not in assigned_bikes:
                worker_bike_pos[worker] = bike
                assigned_bikes.add(bike)
                
            if len(assigned_bikes) == len(workers):
                return worker_bike_pos

        return worker_bike_pos
