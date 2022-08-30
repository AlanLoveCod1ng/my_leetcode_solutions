class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hashtable = {}
        components = n
        for i in edges:
            node1, node2 = i
            if node1 in hashtable and node2 in hashtable:
                set1 = hashtable[node1]
                set2 = hashtable[node2]
                if set1 != set2:
                    for i in set2:
                        set1.add(i)
                        hashtable[i] = set1
                    hashtable[node2] = set1
                    components -= 1
            elif node1 in hashtable and not node2 in hashtable:
                set1 = hashtable[node1]
                set1.add(node2)
                hashtable[node2] = set1
                components -= 1
            elif node2 in hashtable and not node1 in hashtable:
                set2 = hashtable[node2]
                set2.add(node1)
                hashtable[node1] = set2
                components -= 1
            else:
                new_set = set([node1,node2])
                hashtable[node1] = new_set
                hashtable[node2] = new_set
                components -= 1
        return components
                