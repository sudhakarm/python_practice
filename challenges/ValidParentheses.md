**Valid Parentheses**
#This is a practice problem in turing.
#Disclaimer: Im not sure if this solution passess all their test cases. use at your own risk.

**##Problem:**
Given a string 's' containing just the characters (, ), [, ], {, and } . Determine if the input string is valid.
Valid only if:
  - Open bracket must be closed by the same type of bracket.
  - Open bracket must be closed in the correct order.


Constraints:
  1 <= s.length <=104
  s contains parentheses only '[](){}'

Example 1:
  Input: s = "()"
  Output: valid

Example 2:
  Input: s = "()[]{}"
  Output: valid

Example 3:
  Input: s = "([})"
  Output: invalid

Example 4:
  Input: s = "([{}])"
  Output: valid
