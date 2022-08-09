class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        totalDam = 0
        highestDam = 0
        for i in range(len(damage)):
            totalDam += damage[i]
            highestDam = max(highestDam, damage[i])
        
        return 1 + totalDam - highestDam + max(0, highestDam - armor)