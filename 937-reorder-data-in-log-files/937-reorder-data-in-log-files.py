class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_list = []
        digit_list = []
        for log in logs:
            current = Log(log)
            if current.is_letter:
                letter_list.append(current)
            else:
                digit_list.append(current)
        letter_list.sort()
        log_list = letter_list + digit_list
        res = [log.string for log in log_list]
        return res
        
        
class Log:
    def __init__(self,log_str):
        strs = log_str.split(" ")
        self.string = log_str
        self.identifier = strs[0]
        self.contents = strs[1:]
        self.contentsStr = " ".join(self.contents)
        self.is_letter = not strs[1].isdigit()
    
    def __lt__(self, other):
        if not self.is_letter or not other.is_letter:
            return False
        if self.contentsStr != other.contentsStr:
            return self.contentsStr < other.contentsStr
        return self.identifier < other.identifier