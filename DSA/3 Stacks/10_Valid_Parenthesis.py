class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        paren = { ")" : "(", "]": "[", "}": "{"}

        for c in s:
          if c in paren: 
            if stack and stack[-1] == paren[c]:
              stack.pop()
            else: 
              return False
          else:
            stack.append(c)
          
        if not stack:
          return True
        
        else: 
          return False

