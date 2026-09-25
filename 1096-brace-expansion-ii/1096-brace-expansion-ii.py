class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:

        def multiply(a, b):
            result = set()

            for x in a:
                for y in b:
                    result.add(x + y)

            return result

        def parse(i):
            result = set()
            current = {""}

            while i < len(expression) and expression[i] != '}':
                
                if expression[i] == '{':
                    inside, i = parse(i + 1)
                    current = multiply(current, inside)

                elif expression[i] == ',':
                    result.update(current)
                    current = {""}
                    i += 1

                else:
                    current = multiply(current, {expression[i]})
                    i += 1

            result.update(current)

            if i < len(expression) and expression[i] == '}':
                i += 1

            return result, i

        result, _ = parse(0)

        return sorted(result)