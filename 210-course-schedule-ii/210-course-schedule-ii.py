class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build graph
        # direction of edge advance -> basic
        # the most advanced course is the root, there is no other course point to it
        # if there is not root, cycle exists, that is, impossible to take all courses
        # current : [list of its prerequisites]
        hash_table = {}
        degree = {} # number of prerequest 
        #construct graph
        for i in range(len(prerequisites)):
            advance, basic = prerequisites[i] #[advance, basic] basic is prerequisit of advance
            temp_list = hash_table.get(basic,[]) # e.g. {1:[2,3]} temp_list : [2,3] is the advance of 1
            temp_list.append(advance) # advance = 4 temp_list [2,3,4]
            hash_table[basic] = temp_list # {1:[2,3,4]} 2,3,4 need 1 as pre
            degree[advance] = degree.get(advance,0)+1 # increase the degree of the advance
        
        
        start_course = []
        for i in range(numCourses):
            if not i in degree:
                start_course.append(i)
                
        queue = deque(start_course)

        res = []
        while queue:
            current = queue.popleft()
            res.append(current)
            parents = hash_table.get(current,[])
            
            for parent in parents:
                degree[parent] = degree[parent]-1
                # if degree of this parent is 0, which means
                # we have 0 unfinished pre, so we can take it now
                if degree[parent] == 0:
                    queue.append(parent)
        # if there is cycle, some course would left degree != 0, when we break the loop
        # so return []
        return res if len(res) == numCourses else []
        