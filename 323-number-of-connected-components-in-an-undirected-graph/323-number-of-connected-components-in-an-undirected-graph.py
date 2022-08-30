class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def find(current):
            if representative[current] == current:
                return current
            representative[current] = find(representative[current])
            return representative[current]
        def combine(comp1,comp2):
            re1 = find(comp1)
            re2 = find(comp2)
            if re1 == re2:
                return 0
            else:
                if size[re1] > size[re2]:
                    size[re1] += size[re2]
                    representative[re2] = re1
                else:
                    size[re2] += size[re1]
                    representative[re1] = re2
            return 1
        representative = []
        size = []
        res = n
        for i in range(n):
            representative.append(i)
            size.append(1)
        for edge in edges:
            v1, v2 = edge
            res -= combine(v1,v2)
        return res