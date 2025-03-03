class ExpressionEvaluator:
    def __init__(self):
        self.stack = []
        self.undefined_flag = False

    def _precedence(self, operator):
        if operator == '+' or operator == '-':
            return 1
        elif operator == '*' or operator == '/':
            return 2
        return 0

    def _apply_operator(self, operator):
        try:
            operand2 = self.stack.pop()
            operand1 = self.stack.pop()
            if isinstance(operand1, str) or isinstance(operand2, str):
                self.undefined_flag = True
                return
            if operator == '+':
                self.stack.append(operand1 + operand2)
            elif operator == '-':
                self.stack.append(operand1 - operand2)
            elif operator == '*':
                self.stack.append(operand1 * operand2)
            elif operator == '/':
                if operand2 == 0:
                    self.undefined_flag = True
                else:
                    self.stack.append(operand1 / operand2)
        except IndexError:
            self.stack.append("Invalid expression")

    def evaluate_expression(self, expression):
        try:
            self.undefined_flag = False
            operators = set(['+', '-', '*', '/'])
            postfix_tokens = []
            self.stack.clear()

            for token in expression.split():
                if token.isnumeric():
                    postfix_tokens.append(float(token))
                elif token in operators:
                    while (
                        self.stack and
                        self._precedence(token) <= self._precedence(self.stack[-1])
                        and self.stack[-1] != '('
                    ):
                        postfix_tokens.append(self.stack.pop())
                    self.stack.append(token)
                elif token == '(':
                    self.stack.append(token)
                elif token == ')':
                    while self.stack and self.stack[-1] != '(':
                        postfix_tokens.append(self.stack.pop())
                    if not self.stack or self.stack[-1] != '(':
                        return "Mismatched parentheses"
                    self.stack.pop()
            postfix_tokens.extend(reversed(self.stack))
            self.stack.clear()

            for token in postfix_tokens:
                if isinstance(token, float):
                    self.stack.append(token)
                elif token in operators:
                    self._apply_operator(token)

            if self.undefined_flag:
                return "Undefined: number divided by 0"
            if len(self.stack) == 1 and isinstance(self.stack[0], float):
                return self.stack[0]
            elif len(self.stack) == 1 and isinstance(self.stack[0], str):
                return self.stack[0]
            else:
                return "Invalid expression"
        except:
            return "Invalid expression"

expression_evaluator = ExpressionEvaluator()

result1 = expression_evaluator.evaluate_expression("3 + 5 * 2")
print("Result 1:", result1)  

result2 = expression_evaluator.evaluate_expression("( 3 + 5 ) * 2 2")
print("Result 2:", result2)

result3 = expression_evaluator.evaluate_expression("3 * ( 2 + 5 ) / 0 - 1")
print("Result 3:", result3)