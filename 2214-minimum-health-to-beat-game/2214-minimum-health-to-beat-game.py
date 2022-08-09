class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        totalDam = sum(damage)
        highestDam = max(damage)
        return 1 + totalDam - highestDam + max(0, highestDam - armor)