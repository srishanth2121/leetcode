class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        # Convert knowledge into a dictionary
        d = {}

        for key, value in knowledge:
            d[key] = value

        result = ""
        i = 0

        while i < len(s):

            if s[i] == '(':
                i += 1
                key = ""

                
                while s[i] != ')':
                    key += s[i]
                    i += 1

                
                if key in d:
                    result += d[key]
                else:
                    result += "?"

                i += 1

            else:
                result += s[i]
                i += 1

        return result