class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            curr_asteroid_destroyed = False

            # possible collision when curr asteroid going left and prev asteroid going right
            while stack and stack[-1] > 0 and asteroid < 0:
                # if equal size, prev and curr both destroyed
                # no more other collisions
                if stack[-1] == -asteroid:
                    curr_asteroid_destroyed = True
                    stack.pop()
                    break

                # if curr greater than prev, prev destroyed
                # possibly more collisions
                elif stack[-1] < -asteroid:
                    stack.pop()
                
                # if curr less than prev, curr destroyed
                # no more other collisions
                else:
                    curr_asteroid_destroyed = True
                    break

            # only add curr if curr not destroyed by prev (curr > prev)
            if not curr_asteroid_destroyed:
                stack.append(asteroid)
        return stack
