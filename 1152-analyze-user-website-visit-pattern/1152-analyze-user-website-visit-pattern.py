class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # time complexity O(N) space O(N)
        
        user_indices = {} #{str : []} -> {name : list of indices}
        for i in range(len(username)):
            temp_list = user_indices.get(username[i], []) #{'joe':[1,2]} temp_list = [1,2]
            temp_list.append(Visit(username[i],timestamp[i],website[i])) #[1,2] -> [1,2,3]
            user_indices[username[i]] = temp_list # {'joe':[1,2,3]}
        
        pattern_occur = {}
        max_occur = 0 # occur of res
        res = []
        for username in user_indices:
            visits = user_indices[username] # this is the list of indices of apperance
            visits = sorted(visits) # sort the visit to make following the increasing timestamp sequence
            current_website = [visit.website for visit in visits] # website visited by this user in sequence of timestamp
            # no pattern
            if len(current_website) < 3:
                continue
            # build sliding window

            visited = set([])# check whether this pattern is already visited by this user, avoid add twice for one user
            for i in range(len(current_website)-2):
                for j in range(i+1,len(current_website)-1):
                    for z in range(j+1,len(current_website)):
                        pattern = tuple([current_website[i],current_website[j],current_website[z]])
                        if not pattern in visited:
                            pattern_occur[pattern] = pattern_occur.get(pattern,0)+1

                            #update the res
                            if pattern_occur[pattern] > max_occur:
                                max_occur = pattern_occur[pattern]
                                res = pattern
                            # if same occur, select the pattern with lexgraphically smaller one
                            elif pattern_occur[pattern] == max_occur:
                                res = min(res, pattern)

                            visited.add(pattern)
        return res
class Visit:
    def __init__(self,username,timestamp,website):
        self.username = username
        self.timestamp = timestamp
        self.website = website
    def __lt__(self,other):
        return self.timestamp < other.timestamp
            