class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]],
                   containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        visited = [False] * n
        has_box = [False] * n

        for box in initialBoxes:
            has_box[box] = True

        total = 0
        changed = True

        while changed:
            changed = False
            for box in range(n):
                if has_box[box] and not visited[box] and status[box] == 1:
                    visited[box] = True
                    total += candies[box]
                    candies[box] = 0
                    changed = True

                    for key in keys[box]:
                        status[key] = 1  # Unlock box

                    for contained in containedBoxes[box]:
                        has_box[contained] = True

        return total
