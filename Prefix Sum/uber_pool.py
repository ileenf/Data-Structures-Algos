class Solution:
    def uber_pool(self, trips, capacity):
        prefixes = [0 for _ in range(max(trip[1] for trip in trips)+1)]

        for start_x, end_x, num_passengers in trips:
            prefixes[start_x] += num_passengers
            prefixes[end_x] -= num_passengers

        total_num = 0
        for num in prefixes:
            total_num += num
            if total_num > capacity:
                return False
        return True
