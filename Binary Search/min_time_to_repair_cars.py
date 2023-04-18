import math
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def time_within(ranks, cars, time):
            num_cars = 0
            for rank in ranks:
                n = math.floor((time/rank)**0.5)
                num_cars += n

            return num_cars >= cars

        start = 1
        end = cars**2 * max(ranks)


        while start < end:
            time = (start + end) // 2

            if time_within(ranks, cars, time):
                end = time
            else:
                start = time + 1 
        return start
