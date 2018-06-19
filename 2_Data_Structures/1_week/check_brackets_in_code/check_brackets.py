# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

def match_brackets(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            opening_brackets_stack.append(Bracket(next, i + 1))

        if next == ')' or next == ']' or next == '}':
            if opening_brackets_stack:
                open_bracket = opening_brackets_stack.pop()
            else:
                return i + 1
            if (open_bracket.Match(next)):
                continue
            else:
                return i + 1
    if opening_brackets_stack:
        return opening_brackets_stack[0].position
    else:
        return "Success"

if __name__ == "__main__":
    text = sys.stdin.read()
    print(match_brackets(text))
