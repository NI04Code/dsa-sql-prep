# https://leetcode.com/problems/simplify-path

class Solution:
    def simplifyPath(self, path: str) -> str:
        ls_path = [p for p in path.split("/") if p]
        i = 0
        while i < len(ls_path):
            if i == 0 and ls_path[i] == "..":
                ls_path.pop(i)
            elif i != 0 and ls_path[i] == "..":
                ls_path.pop(i)
                ls_path.pop(i-1)
                i -= 1
            elif ls_path[i] == ".":
                ls_path.pop(i)
            else:
                i += 1
        
        output = ""
        for p in ls_path:
            if p:
                output += "/" + p
        
        if output == "":
            output += "/"

        return output