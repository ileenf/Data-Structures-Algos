# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    # time complexity: O(n) iterate n - 1 times, each iteration will remove one element.
    # popping and adding to set is constant time. 
    # iterating over n people at the end. O(n) + O(n) = O(n)
    # space complexity: O(n), storing n people in set
    def findCelebrity(self, n: int) -> int:
        people = {i for i in range(n)}
        
        while len(people) > 1:
            p1 = people.pop()
            p2 = people.pop()
            
            if knows(p1, p2):
                people.add(p2)
            else:
                people.add(p1)
        
        potential_celeb = people.pop()
        
        for p in range(n):
            if p != potential_celeb:
                if not knows(p, potential_celeb):
                    return -1
                if knows(potential_celeb, p):
                    return -1
        return potential_celeb
        
