class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        
        def backtrack(open_count: int, close_count: int, current_str: str):
            # Base case: valid combination found
            if len(current_str) == 2 * n:
                res.append(current_str)
                return
            
            # Can add an opening parenthesis if we haven't reached n
            if open_count < n:
                backtrack(open_count + 1, close_count, current_str + "(")
                
            # Can add a closing parenthesis if it matches a previous open one
            if close_count < open_count:
                backtrack(open_count, close_count + 1, current_str + ")")
                
        backtrack(0, 0, "")
        return res