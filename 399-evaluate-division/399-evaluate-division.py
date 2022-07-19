from collections import deque
class Currency:
    def __init__(self,name):
        self.name = name
        self.exchanges = {}
        
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        currency_map = {}
        for i in range(len(equations)):
            cur1 = currency_map.get(equations[i][0], Currency(equations[i][0]))
            cur2 = currency_map.get(equations[i][1], Currency(equations[i][1]))
            cur1_cur2 = values[i]
            cur1.exchanges[cur2] = cur1_cur2
            cur2.exchanges[cur1] = 1/cur1_cur2
            currency_map[equations[i][0]] = cur1
            currency_map[equations[i][1]] = cur2
        result = []
        for query in queries:
            result.append(self.bfs(currency_map,query[0],query[1]))
        return result
    
    def bfs(self, currency_map, start, target):
        if not start in currency_map or not target in currency_map:
            return -1
        visited = set([currency_map[start]])
        queue_v = deque([currency_map[start]])
        queue_w = deque([1])
        while queue_v:
            current = queue_v.popleft()
            current_weight = queue_w.popleft()
            visited.add(current)
            if current.name == target:
                return current_weight
            for child in current.exchanges:
                if child in visited:
                    continue
                queue_v.append(child)
                queue_w.append(current_weight*current.exchanges[child])
        return -1